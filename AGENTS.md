# AGENTS.md

Guidance for agents and contributors working in this repo. It governs how skills are
written so they stay consistent, portable, and on-brand. The brand is simple: content
that doesn't read like AI.

## What this repo is

A collection of Agent Skills for blogging. Each skill is a folder under `skills/` with
a `SKILL.md` and optional `references/`. Skills are model-invoked: the agent matches
the user's request against each skill's `description` and loads the best fit. They also
work as slash commands (`/article`, `/humanize`).

## Skill structure

```
skills/<name>/
├── SKILL.md          # required, under 500 lines
└── references/       # optional, loaded on demand
```

- Frontmatter has exactly `name` and `description`, plus a `metadata` block with
  `version`.
  - `name`: lowercase, hyphenated, matches the folder name (1 to 64 chars).
  - `description`: the trigger, and the most important field. It does three jobs:
    (1) what the skill does, (2) the phrases a user would say to invoke it ("Also use
    when the user says '...'"), and (3) scope boundaries pointing to sibling skills
    ("For X, see Y."). The agent routes on this.
- Body: an H1 title, a second-person role line, an "Initial assessment" that reads
  shared context first, a numbered method, an "Output" section, and a "Related skills"
  line.
- Keep `SKILL.md` under 500 lines. Move depth into `references/` and link to it.

## The foundation contract

Two skills are read first by every writing skill:

- `blog-context` writes `.agents/blog-context.md` (niche, audience, voice). Every
  skill's "Initial assessment" reads it, so the user explains their blog once.
- `house-style` owns `references/ai-tells.md`, the writing rulebook. Every skill that
  produces prose loads it before drafting.

## The rulebook is duplicated on purpose

`references/ai-tells.md` is the crown jewel. The canonical copy lives in `house-style/`.
`humanize/` and `article/` each bundle a copy so they work when installed alone. If you
edit the canonical file, re-sync the copies (`cp skills/house-style/references/ai-tells.md
skills/humanize/references/ai-tells.md`, and the same for `article/`). `scripts/validate.py`
fails if they drift.

`house-style` is the required foundation: every skill that writes prose reads its
rulebook. `youtube-to-blog` also builds on `article` (it reuses `article/references/`).
The default install (the whole collection) satisfies these. Installing a single writing
skill standalone works only for the three that bundle the rulebook: `house-style`,
`humanize`, and `article`.

## Writing style for skills

Write the skills the way the skills tell models to write. No em dashes in the body,
straight quotes, sentence-case headings, prose over bold-colon bullets, no emoji,
second person, short and scannable. Em dashes are allowed only inside the frontmatter
`description` (dense matching text, not reader-facing prose), matching the convention
these files already use.

## Portability

Keep `SKILL.md` files vanilla markdown so they run across agents (Claude Code, Codex,
Cursor, Windsurf). Don't add Claude-Code-only syntax to a `SKILL.md`; other agents
would print it literally. Note that `article` and `youtube-to-blog` link to
`article/references/` files via relative paths, so they assume `article` is installed
alongside (the default when you install the whole collection).

## Versioning

Each skill carries `metadata.version` (semver). The repo version and the per-skill
table live in `VERSIONS.md`. Bump a skill's version when its behavior changes, and keep
`VERSIONS.md`, `.claude-plugin/plugin.json`, and `.claude-plugin/marketplace.json` in
sync on a release.

## Validation

Run `python3 scripts/validate.py` before any release. It checks frontmatter, the
500-line budget, body hygiene (no em dashes or unicode arrows in prose), that every
"Related skills" reference resolves to a real skill, that the bundled `ai-tells.md`
copies are in sync, and that the manifests and `VERSIONS.md` table are consistent.
