# AI writing tells to avoid

This is the house anti-slop standard. Every writing skill in this collection reads
it before drafting or editing. It catalogs the words, sentence shapes, and
structural habits that make text read as machine-made, with the fix for each.

It comes from editing a high volume of model-generated drafts and tracking which
patterns readers reliably clock as "a bot wrote this." Treat it as a contract, not
a list of suggestions.

## How to read these rules

**Judge by frequency, not single instances.** Most of what follows is a tell only
when it repeats. One em dash is invisible; a dozen is a fingerprint. One rhetorical
question can land; six in a row patronize the reader. Flag clusters and habits, not
the occasional honest use. The word bans below are the exception — those come out
on sight.

**A real voice outranks these rules.** If the author's documented voice (see
`blog-context.md`) uses fragments, parallel structure, or rhetorical questions on
purpose, keep them. These rules target the reflexes no human reaches for unprompted.
They are not a license to flatten every draft to the same surface.

---

## Words and phrases to cut

**Model vocabulary.** Words that cluster in AI prose far more than in human writing.
Cut unless it's genuinely the exact word you need: delve, leverage (as a verb),
utilize, robust, seamless, streamline, harness, foster, elevate, unlock, embark,
navigate (as metaphor), realm, landscape (as metaphor), tapestry, ecosystem,
paradigm, synergy, holistic, cutting-edge, game-changer, pivotal, resonate,
intricate, crucial, vital, invaluable, transformative. Use the word you'd say out
loud.

**Verbs that fake weight.** Plain "is" and "are" beat "serves as," "stands as,"
"represents," "embodies," "marks."
- Heavy: "The dashboard serves as the team's single source of truth."
- Plain: "The dashboard is the team's source of truth."

**Adverbs that inflate.** quietly, deeply, fundamentally, remarkably, arguably. They
paint an ordinary statement as a profound one. Delete them, or prove the point.

**Grand nouns for plain things.** "tapestry" for anything woven together,
"landscape" for any field, "realm" for any area, "journey" for any process. Name the
actual thing.

**Coined jargon.** Analytical-sounding compounds that were never actually defined:
"the alignment paradox," "the engagement trap," "scope creep" used as if it explains
itself. Make the argument; don't smuggle it in as a label.

**Fake ranges.** "From X to Y" only works when X and Y mark the ends of a real scale.
"Everything from spreadsheets to company culture" isn't a range, it's two things.
List them.

**Sourceless claims.** "experts say," "studies show," "research suggests," "many
believe." If you can't name who, you don't have a source. Name it or drop the claim.

---

## Sentence-level tics

**Negative-then-positive reframes — the most common single tell.** "It's not X, it's
Y." / "This isn't about A; it's about B." Plus the staccato version, "Not louder. Not
flashier. Just better." and the cross-sentence form, "The problem was never the
budget. The problem was the plan."
- Tell: "It's not a feature. It's a philosophy."
- Fix: state the point straight. One reframe per piece, at most.

**Question, then a clipped answer.** Posing a question nobody asked and snapping back
a fragment for drama. Includes the how-to version: "Need it faster? Cache it."
- Tell: "The catch? There's always a catch." / "Want cleaner data? Validate on input."
- Fix: "There's always a catch." / "To get cleaner data, validate on input."

**Same opening, three times running.** "They want speed. They want polish. They want
it yesterday." One deliberate parallel set is fine; a wall of them is a pattern.

**Stacked threes.** The rule of three works once. Three triples back to back ("Plan,
build, ship. Test, learn, adjust. Scale, refine, repeat.") reads like a machine that
found a groove. Use one, then move on.

**Participle padding.** Tacking "-ing" clauses onto a sentence to manufacture
significance: "...cementing its place in the market," "...reflecting a broader
shift," "...highlighting the need for change." End on the fact.

**Throat-clearing transitions.** "It's worth noting," "Importantly," "Notably,"
"Interestingly." They announce significance instead of delivering it. Cut them and
the sentence gets stronger.

---

## Rhythm and paragraphs

**Fragments posing as paragraphs.** "And it worked. Every time." A one-line fragment
dropped in for weight. Real people write in sentences; use them.

**A list wearing a suit.** Prose that's secretly a list: "First, there's cost.
Second, there's speed. Third, there's support." Either commit to a list or write real
connected prose with transitions.

**Sentence length.** Keep most sentences under 20 words, averaging around 12 to 17.
Let no more than a quarter run long. The variation itself — short, short, long, short
— is what reads as human. Uniform length reads as generated.

**Vary how sentences start.** Never open three in a row with the same word.
- Flat: "The tool tracks spend. The tool flags overages. The tool emails you."
- Varied: "The tool tracks spend. It flags overages automatically. You get an email
  the moment one hits."

**Reading level.** Aim for roughly 8th-to-9th-grade ease. Mostly active voice; keep
passive under about 10 percent.

---

## Tone tells

**Manufactured suspense.** "Here's the thing." "Here's the kicker." "Here's where it
gets interesting." "But here's what nobody tells you." Make the point without the
drumroll.

**Lecturing the reader.** "Let's break this down." "Let's unpack that." "Let's dive
in." You're not running a seminar. Just say it.

**Reach-y analogies.** "Think of it like a..." / "It's basically a..." usually muddies
more than it clears and defaults to teacher mode. Explain it plainly first; reach for
the analogy only if it truly helps.

**"Imagine a world where..."** followed by a wishlist. Open with something real.

**Performed honesty.** "I'll be honest with you." "Full transparency:" "This might be
controversial, but..." Real candor is specific and a little uncomfortable; the
manufactured kind is smooth and risk-free. Cut it.

**Announcing instead of showing.** "The truth is simple." "Make no mistake." "The
reality is clear." If you have to declare your point obvious, it isn't yet. Show it.

**Overblown stakes.** Not everything is era-defining. "will change the game forever,"
"reshapes how we think about work," "the most important shift of our lifetime." Keep
the claim the size of the evidence.

**Concede-and-dismiss.** "While there are challenges, the upside is undeniable."
Raising an objection only to wave it off. Engage it or leave it out.

---

## Formatting tells

**Em-dash habit.** Models lean on em and en dashes (—, –) as a rhythm crutch,
especially in short copy. Default to a comma, a colon, parentheses, or two sentences.
(Exception: a voice that uses them on purpose.)

**Label-colon bullets.** Every list item opening with a **bolded label:** then an
explanation. Almost no one writes lists this way by hand. Use plain sentence-form
items, or vary the shape.

**Decorative unicode.** Curly quotes and arrows (→, ⇒) give away machine output. Use
straight quotes and "->" or rewrite. (The publishing layer should normalize these
anyway.)

**No horizontal rules.** Don't slice sections with `---`. Headings already do that
job.

**Headings.** Use H2 and H3 (H4 only if truly needed), and never skip a level. Drop
generic labels like "Introduction," "Overview," or "Key Takeaways." Each heading
should say what the reader gets in that section. Don't number or prefix them. Work
keywords in only where they read naturally.

**Lists are the exception; prose is the default.** More than two or three lists in a
post means you're leaning on them. Reserve lists for real sequences or
quick-reference items. Don't nest them.

**Bold sparingly.** A key phrase here and there, never whole sentences, never every
other line.

**Tables only for tabular data.** Side-by-side specs or comparisons, yes. A table to
dress up prose, no. Set it up with a sentence and state the takeaway after.

---

## Whole-piece tells

**Announced endings.** "In conclusion," "To sum up," "In summary," "At the end of the
day," "All in all." Good writing lands the ending without flagging it.

**Recaps inside recaps.** Telling the reader what you'll cover, covering it, then
summarizing it — at every level of the piece. Say it once.

**The beaten metaphor.** Introducing one image and riding it through the whole article
(every paragraph circling back to "the engine room"). Use it once, then let it go.

**Name-drop stacking.** Rapid-fire references to borrow authority: "Amazon did it.
Netflix did it. Spotify did it." One example made well beats five dropped in a row.

**One idea, stretched.** Inflating a tight 600-word point into 2,000 by restating it
in new outfits. Make each point once, then stop.

**Duplicated sections.** The same point delivered nearly verbatim later in the piece —
a giveaway of unedited long generation. Check for it before shipping.

---

## Titles

- Lead with the primary keyword and keep it under ~60 characters.
- Promise one concrete benefit, not a vague vibe. "Cut your AWS bill in 30 days" beats
  "Thinking about cloud costs."
- Match the actual article. Don't say "9 ways" unless nine are there.
- Skip the AI title molds: "The Ultimate Guide to...," "Everything You Need to Know
  About...," "Unlocking the Power of...," "X Things You Need to Know," "Mastering the
  Art of...," "Why X Is the Future of Y."
- Drop empty superlatives ("the best way," "the only X you'll ever need," "the secret
  to") and filler words ("really," "actually," "simply," "just").

## Introductions

- 3 to 5 sentences, under 150 words, in 2 or 3 short paragraphs. Never one dense block.
- Hook, then context, then a turn into the body. Lead with the reader's problem and
  make the payoff clear early.
- Skip the stock openers: "In today's fast-paced world," "It's no secret that," "In an
  era of," "Whether you're a beginner or a pro." No dictionary definitions. No "In this
  post, you'll learn: 1, 2, 3."

## Conclusions

- Its own section, the last one. Reinforce the single biggest takeaway — don't relist
  every point.
- Tie back to the opening.
- Add a CTA only if it genuinely fits. For an explainer or analysis, skip it.
- Avoid the signposted closers above; deliver the last thought directly.

## FAQ (optional)

- 3 to 5 questions a real person would actually type into Google or an AI assistant.
- Each question is an H3; answers run 2 to 4 sentences, answer first.
- Don't restate the question inside the answer, and don't open every one with "Yes" or
  "No." Vary them. No rules between questions.

## Links

- Markdown with descriptive anchor text, 2 to 6 words. Never a bare URL on its own
  line, never "click here," "read more," or "this article."
- Link only where it helps the reader act on the sentence they're reading. Editorial
  value first. Prefer a deep page over a homepage.
- One link per destination, absolute URLs, roughly one internal link per 300 words.

---

## Quick self-check before shipping

- Search the draft for: — (em dash), "serves as," "it's not," "here's the," "in
  conclusion," "let's dive," "delve," "landscape," "→," and bolded-label bullets. Each
  hit is a candidate to cut or rewrite.
- Read any three sentences in a row out loud. Different opening words? Different
  lengths?
- Could a sentence sit unchanged in a competitor's post on the same topic? Sharpen it
  or cut it.
- Did you make each point once, or dress the same one up five times?
