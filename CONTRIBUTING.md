# Contributing

New skills and improvements are welcome. See [AGENTS.md](AGENTS.md) for the full
authoring contract.

## Improving a skill

1. Read the skill's `SKILL.md` and `skills/house-style/references/ai-tells.md`.
2. Make the change. Keep `SKILL.md` under 500 lines; move depth into `references/`.
3. Run the skill's own advice on its own text: no em dashes in the body, no AI-ese,
   sentence case, prose over bold-colon bullets.
4. Bump `metadata.version` and update `VERSIONS.md`.

## Adding a skill

1. Create `skills/<name>/SKILL.md` with the frontmatter contract in AGENTS.md.
2. Make the `description` specific: what it does, the trigger phrases, and the scope
   boundaries to sibling skills.
3. Have its "Initial assessment" read `.agents/blog-context.md` and, if it writes
   prose, the house-style rulebook.
4. Add it to the table in `README.md` and to `VERSIONS.md`.
5. Cross-link it from related skills' "Related skills" lines.

## Validation and tests

Run `python3 scripts/validate.py` before opening a PR. It checks structure, body
hygiene, cross-references, the bundled `ai-tells.md` sync, and the manifests. The
intended routing for common prompts lives in `tests/routing-cases.json`; add a case
when you add a skill, and re-check routing (have an agent pick a skill for each prompt
using only the descriptions) when you change a trigger.

## The bar

Every skill should make content that ranks and doesn't read like AI. If a change makes
the output sound more like a machine, it doesn't ship.
