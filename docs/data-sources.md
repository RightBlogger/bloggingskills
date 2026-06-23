# Data sources

Every skill in this collection works with zero tools connected. Each one reasons
from its own knowledge, and that gets you a real draft, a sane keyword set, a
plausible read of the competition. Connecting a data source does not unlock the
skill. It makes the skill sharper and grounds it in your actual numbers instead of
its best guess.

The rule the skills follow: use a connected source when one is present, and fall
back to reasoning when it is not. They never fabricate data to fill the gap. A
skill that cannot see your Search Console will infer the keywords a searcher would
type and tell you it inferred them. It will not hand you invented search volumes
that look like they came from somewhere.

This page maps each skill to the kind of data source that helps it, so you know
what is worth wiring up for the work you do most. The tools named in parentheses
are examples, not requirements. Any source in the same category does the job.

## What helps which skill

| Skill | Data-source category | What it unlocks |
|-------|---------------------|-----------------|
| keyword-research | search analytics / keyword data (Google Search Console, a keyword research API or MCP) | Real search volumes, difficulty scores, and the queries your site already ranks for, instead of inferred term lists. |
| seo-optimize | search analytics / keyword data (Google Search Console, a keyword API or MCP) | The terms a page already gets impressions for, so the optimization pass targets demand that exists rather than demand it assumes. |
| meta | search analytics / keyword data (Google Search Console, a keyword API or MCP) | The actual query and click-through data behind a page, so the title and description are written to win the clicks the page is positioned for. |
| serp-analysis | web search / scraping (a SERP API, a search MCP, a scraping tool) | Reads the live top-ranking results for the keyword instead of guessing what ranks, so the brief reflects what is actually winning today. |
| ai-seo | web search / scraping (a SERP API, a search MCP, a scraping tool) | Pulls how AI answer engines currently frame the topic and who they cite, so the citability work targets real gaps. |
| internal-links | sitemap / CMS index (an XML sitemap, the CMS API) | Links only to pages that exist on your site, with the real URLs, so no anchor points at a guessed or dead path. |
| youtube-to-blog | video transcript (a YouTube transcript tool or MCP) | The actual words from the video, so the post is built from what was said, not from a summary of the title and description. |
| brand-voice | the user's writing samples / CMS archive (past posts, a CMS export, a docs folder) | Captures a real voice from real writing, so matching has something concrete to match instead of a generic register. |
| article | all of the above, through the pipeline | Conducts the research, draft, and optimization steps, so it uses whatever sources are connected at each stage and falls back where they are not. |
| blog-context | the user's site and writing (CMS, sitemap, past posts) | Captures niche, audience, pillars, and voice once, so a richer source means a more grounded context file for every later skill. |
| house-style | none (knowledge only) | The anti-slop rulebook is self-contained. It needs no external data to audit a draft. |
| humanize | none (knowledge only) | Stripping AI tells and restoring voice is a text operation. It reads the draft and, if present, your captured voice, and nothing else. |

Publishing is a near-term capability rather than a shipped skill. When it lands it
will use a CMS write API (WordPress, Ghost, Webflow) to push the finished post
straight to your site, closing the loop from topic to published.

## How to connect a source

These sources are wired into your host coding agent as MCP servers or CLIs, the
same way you connect anything else it can reach. You do not configure them inside
the skills. The skills auto-detect what the agent can see and use it.

So the setup is on your side: connect a Search Console MCP, a keyword API, a SERP
or scraping tool, your CMS, or a transcript tool to the agent, and the matching
skill starts pulling real data the next time it runs. Connect nothing and every
skill still runs.

The golden rule holds either way. If a source is not connected, the skill infers
from its own knowledge and says so in its output. It does not invent search
volumes, fabricate SERP results, or guess at URLs that might not exist. Grounded
when it can be, honest when it cannot.

## This is guidance, not a dependency

Nothing here is required. The collection is fully usable with no integrations at
all. Treat this page as a map of where connecting a source pays off most, and wire
up only what matches the work you actually do.
