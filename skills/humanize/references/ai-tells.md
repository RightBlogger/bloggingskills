# AI writing tells to avoid

This is the house anti-slop standard. Every writing skill in this collection reads
it before drafting or editing. It catalogs the words, sentence shapes, and
structural habits that make text read as machine-made, with the fix for each.

It comes from editing a high volume of model-generated drafts and tracking which
patterns readers reliably clock as "a bot wrote this." Readers who spot one stop
trusting the rest of the page, and so do the editors and answer engines deciding
what to quote. That is why it matters.

Contents: how to use this rulebook · hard rules · words and phrases · sentence-level
tics · rhythm and paragraphs · tone tells · formatting tells · whole-piece tells ·
the tidy, self-announcing post · titles · introductions · conclusions · FAQ · links ·
quick self-check before shipping.

## How to use this rulebook

The rules come in two tiers, and the difference is the whole point.

**Hard rules apply to every line you write.** They are cheap to avoid, readers
pattern-match them instantly, and several of them show up in search results where
everyone sees them. Aim for zero.

**Frequency tells are judged by repetition.** One rhetorical question can land; six
in a row patronize the reader. One short fragment for emphasis is fine; a fragment
in every paragraph is a fingerprint. Flag clusters and habits, not the occasional
honest use.

**Shape outweighs words.** A post's structure (how it announces itself, how it ends,
whether it says anything specific) gives it away more reliably than its vocabulary:
detectors catch it, readers name it, and rewording leaves it intact. Fix the shape
first; swapping a flagged word for a synonym fixes nothing.

**Writing versus editing.** When you write new copy, write toward the positive
defaults: a particular reader in mind, specific facts, plain words, a clear opinion.
The hard rules apply while you draft; the rest of this file is the checklist you run
on the draft, not a list of words to steer around sentence by sentence. When you
edit someone else's text, fix every hard-rule hit, fix frequency tells only where
they repeat or stack, and leave the rest of the author's choices alone.

**One hit, one rule.** When a phrase breaks two rules, file it under the more
serious one: a hard rule over a shape habit, a shape habit over a frequency tell.

**The user's request outranks this file.** If the user explicitly asks for
something a rule forbids, do what they asked. If that means invented material (a
sample quote, a placeholder statistic), label it as an example so it can't be
mistaken for fact. A captured voice comes next.

**A captured voice outranks both tiers.** If `.agents/blog-context.md` (or a
`voice-<name>.md` profile from brand-voice) lists a habit as intentional, such as
fragments, rhetorical questions, or a signature dash, keep it. A voice covers habits
of style only; it never unlocks fabrication or chatbot residue. Imitate a voice's
anchor lines, never reuse them: a quoted line turns into the same sentence in every
post. These rules target the reflexes no human reaches for unprompted. They are not
a license to flatten every draft to the same surface.

## Hard rules

1. **No em or en dashes in prose.** Models lean on them (—, –) as a rhythm crutch.
   Use a comma, a colon, parentheses, or two sentences. Number ranges take a plain
   hyphen or "to" ("3 to 5"). The only exceptions are a captured voice that uses
   them on purpose and dialogue in languages whose convention opens a spoken line
   with a dash.
2. **Plain ASCII punctuation.** Straight quotes, not curly ones. No unicode arrows
   (→, ⇒); write "->" or rewrite the sentence. The publishing layer may restyle
   quotes later, but the draft stays plain.
3. **No bold-label bullets.** A list where every item opens with a **bolded label:**
   and then an explanation. Almost no one writes lists this way by hand. Use plain
   sentence-form items, or vary the shape.
4. **No horizontal rules inside a post.** Don't slice sections with `---`. Headings
   already do that job.
5. **No model vocabulary used as metaphor.** delve, leverage (as a verb), utilize,
   robust, seamless, streamline, harness, foster, elevate, unlock, unleash, embark,
   embrace, navigate, realm, landscape, tapestry, ecosystem, paradigm, synergy,
   holistic, cutting-edge, groundbreaking, game-changer, pivotal, resonate,
   intricate, crucial, vital, invaluable, transformative, instrumental, relentless,
   masterful, testament, digital age, fast-paced, ever-evolving. The literal sense
   is fine (an ecosystem in a biology post, landscape in a gardening post, leverage
   in a finance post). Otherwise use the word you'd say out loud.
6. **No stock molds.** The title templates and intro openers listed under Titles and
   Introductions, the announced endings under Whole-piece tells ("In conclusion"),
   and the first four habits of the tidy, self-announcing post ("In this post,
   we'll cover," "Gone are the days").
7. **No chatbot residue.** Lines that belong in a chat window, not a post: "Great
   question," "Certainly!", "I hope this helps," "Feel free to reach out," "As of my
   last update," "As an AI," and unfilled placeholders like "[insert example]."
8. **No fabrication.** Never invent a statistic, study, quote, testimonial, test
   result, first-hand experience, author persona, or credential, and never write "we
   tested," "our data," or "in my experience" unless the source material says so. "Experts say," "studies show,"
   and "research suggests" with no name attached are the same problem in a vaguer
   costume. Name the source or drop the claim. Common knowledge in the field (bitter
   espresso is over-extracted) needs no citation; specific numbers, studies, quotes,
   and anything framed as experience do. When a claim needs evidence you don't
   have, cut it from the post and tell the user what's missing.
9. **Never open a prose line with a hyphen.** Markdown renders "- " at the start of a
   line as a bullet. Rewrite the sentence.

## Words and phrases

**Verbs that fake weight.** Plain "is" and "are" beat "serves as," "stands as,"
"represents," "embodies," "marks."
- Heavy: "The dashboard serves as the team's single source of truth."
- Plain: "The dashboard is the team's source of truth."

**Adverbs that inflate.** quietly, deeply, fundamentally, remarkably, arguably,
truly, incredibly, genuinely, honestly. They paint an ordinary statement as a
profound one. Delete them,
or prove the point.

**Grand nouns for plain things.** "journey" for any process, "realm" for any area,
"tapestry" for anything with parts. Name the actual thing.

**Stiff connectors.** moreover, furthermore, additionally, indeed, thus, hence,
consequently, notwithstanding. Nobody says these out loud. Use "and," "so," "but,"
"also," or no connector at all.

**Corporate-therapist language.** "lean into our strengths," "navigate the
complexities of," "hold space for," "show up for your audience," "a powerful
opportunity to grow." It sounds supportive and says nothing. State the concrete
action.

**Hedge stacks.** "may potentially," "could possibly," "it's important to note that,"
"it can be argued that." One honest hedge where you are unsure is fine.
Two in one sentence is fog.

**Coined jargon.** Analytical-sounding compounds that were never defined: "the
alignment paradox," "the engagement trap," "the clarity gap." Make the argument;
don't smuggle it in as a label.

**Fake ranges.** "From X to Y" only works when X and Y mark the ends of a real
scale. "Everything from spreadsheets to company culture" isn't a range, it's two
things. List them.

**Synonym cycling.** Rotating names for one thing to avoid repetition: "the tool,"
then "the platform," then "the solution," then "this powerful software." Readers
start wondering if these are four different products. Pick a name and reuse it.

## Sentence-level tics

**Negative-then-positive reframes, the most common single tell.** "It's not X, it's
Y." / "This isn't about A; it's about B." Plus the staccato version, "Not louder.
Not flashier. Just better.", the cross-sentence form, "The problem was never the
budget. The problem was the plan.", and the tagline tail, "a pipeline, not a
prompt."
- Tell: "It's not a feature. It's a philosophy."
- Fix: state the point straight. One reframe per piece, at most.

**Question, then a clipped answer.** Posing a question nobody asked and snapping back
a fragment for drama. Includes the how-to version: "Need it faster? Cache it."
- Tell: "The catch? There's always a catch." / "Want cleaner data? Validate on input."
- Fix: "There's always a catch." / "To get cleaner data, validate on input."

**Same opening, three times running.** "They want speed. They want polish. They want
it yesterday." One deliberate parallel set is fine; a wall of them is a pattern.

**Stacked threes.** The rule of three works once. Three triples back to back ("Plan,
build, ship. Test, learn, adjust. Scale, refine, repeat.") read like a machine that
found a groove. Use one, then move on.

**Participle padding.** Tacking "-ing" clauses onto a sentence to manufacture
significance: "...cementing its place in the market," "...reflecting a broader
shift," "...highlighting the need for change." End on the fact.

**Throat-clearing transitions.** "It's worth noting," "Importantly," "Notably,"
"Interestingly." They announce significance instead of delivering it. Cut them and
the sentence gets stronger.

## Rhythm and paragraphs

**Fragments posing as paragraphs.** "And it worked. Every time." A one-line fragment
dropped in for weight. Real people write in sentences; use them.

**A list wearing a suit.** Prose that's secretly a list: "First, there's cost.
Second, there's speed. Third, there's support." Either commit to a list or write
connected prose.

**Sentence length.** Write for someone reading on a phone between other things:
most sentences should parse in one pass, and a long one is fine when its content
needs the room. The variation itself (short, short, long, short) is what reads as
human. Uniform length reads as generated, and so does a run of clipped five-word
sentences. As a rough guide, most sentences land under about 20 words, averaging
around 12 to 17, with no more than about a quarter running long. These are targets
for the whole piece, not limits on any one sentence; a hard cap makes prose choppy.

**Vary how sentences start.** Never open three in a row with the same word, and keep
connector openers ("So," "However," "In addition," "As a result") to a handful per
post. Most sentences should start with their subject.
- Flat: "The tool tracks spend. The tool flags overages. The tool emails you."
- Varied: "The tool tracks spend. It flags overages automatically. You get an email
  the moment one hits."

**Paragraph length.** Mostly one to three sentences, rarely four, so a phone screen
never shows a wall of text. Vary it: a run of identical three-sentence paragraphs is
as much a pattern as a wall.

**Reading level.** Aim for roughly 8th-to-9th-grade ease. Mostly active voice
(passive under about 10 percent as a rough guide), and name the actor when it helps
the reader.

## Tone tells

**Manufactured suspense.** "Here's the thing." "Here's the kicker." "Here's where it
gets interesting." "This is where X comes in." "Let that sink in." Make the point
without the drumroll.

**Lecturing the reader.** "Let's break this down." "Let's unpack that." "Let's dive
in." You're not running a seminar. Just say it.

**Reach-y analogies.** "Think of it like a..." usually muddies more than it clears and
defaults to teacher mode. Explain it plainly first; reach for the analogy only if it
helps.

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

**No position.** Balancing every claim so the post never recommends anything. Readers
came for a judgment. Where the evidence points one way, say which way and why.

**Mannered prose.** Metaphor and flourish in place of a plain statement: "a dial worth
turning" for "a parameter worth varying," "this point earns its keep" for "this point
still matters," "the load-bearing assumption," "the through line," "sits at the
intersection of." These phrases display the writer instead of carrying the idea, and
they drag in connotations nobody chose. When a literal phrase exists, use it.

**Compressed shorthand.** The opposite failure, which writers report from some newer
models: dropped articles, undefined acronyms, references the reader can only decode
three sentences later, a sentence that doesn't resolve until its last word. Write
for a smart reader with no context: define a term before you use it, and put the
point first.

## Formatting tells

**Headings.** Use H2 and H3 (H4 only if needed), and never skip a level. Each
heading says what the reader gets in that section, so drop generic labels like
"Introduction," "Overview," "Conclusion," or "Final thoughts." Keep emoji and
decorative prefixes out. A summary block, when a long reference post earns one (see
the tidy, self-announcing post), may carry a plain label such as "Key takeaways."
Number headings only when the numbers mean something: the steps of a how-to or the
entries of a list post. Work keywords in only where they read naturally.

**Lists are the exception; prose is the default.** More than two or three lists in a
post means you're leaning on them. Reserve lists for real sequences or
quick-reference items. Don't nest them.

**Bold sparingly.** A key phrase here and there, never whole sentences, never every
other line.

**Tables only for tabular data.** Side-by-side specs or comparisons, yes. A table to
dress up prose, no. Set it up with a sentence and state the takeaway after.

## Whole-piece tells

**Announced endings.** "In conclusion," "To sum up," "In summary," "At the end of the
day," "All in all." Good writing lands the ending without flagging it.

**Recaps inside recaps.** Telling the reader what you'll cover, covering it, then
summarizing it, at every level of the piece. Say it once.

**The beaten metaphor.** Introducing one image and riding it through the whole article
(every paragraph circling back to "the engine room"). Use it once, then let it go.

**Name-drop stacking.** Rapid-fire references to borrow authority: "Amazon did it.
Netflix did it. Spotify did it." One example made well beats five dropped in a row.

**One idea, stretched.** Inflating a tight 600-word point into 2,000 by restating it
in new outfits. Make each point once, then stop.

**Duplicated sections.** The same point delivered nearly verbatim later in the piece,
a giveaway of unedited long generation. Check for it before shipping.

**Generic everywhere.** Sentences that could sit unchanged in any competitor's post on
the topic. The cure is specifics only this piece has: a number, a named tool, a real
example, a clear opinion.

## The tidy, self-announcing post

Model-written blog posts share one structure, and it survives any amount of word
swapping. In a September 2026 study of 13,500 company blog posts (SlopShape,
arXiv 2609.15369), a classifier reading structure alone, with every wording feature
removed, scored 97 out of 100 at telling AI posts from human ones. The habits below
had the widest gaps between the two.

The first four carry no information, so fix them wherever they appear, like a hard
rule. The last two are judgment calls: when you write, avoid them; when you edit,
fix what you can without adding material, and flag the rest for the author.

**Announcing the flow.** A roadmap paragraph that lists what's coming ("In this
post, we'll cover X, Y, and Z"). Start on the substance; the headings show the
route. A direct answer in the intro is not this; keep it.

**A summary stage.** A "Key takeaways" box, a recap section, or a closing synthesis
that repeats the body. A separate summary block belongs only on a long reference
piece (roughly 2,000 words or more, or a page readers come back to look things
up), and then keep the close from recapping too.

**A close that recaps.** The conclusion repeats the opening or relists the body. End
on something new: the next step, a caveat, a status, the last real point.

**Old way versus new way.** Setting the topic against a legacy approach nobody in
the post defends ("Gone are the days...", "Traditionally... but today"). Describe
the thing on its own terms.

**Nothing for the reader to do.** No link, tool, template, number, or step the
reader can use. Give them one.

**A confident, institutional voice throughout.** No aside, no admitted doubt, no
register shift. Let the recorded voice show a person wrote it: a real opinion, an
admitted limit, an aside the draft can support.

## Titles

- Lead with the primary keyword and keep it under about 60 characters.
- Promise one concrete benefit, not a vague vibe. "Cut your AWS bill in 30 days" beats
  "Thinking about cloud costs."
- Match the actual article. Don't say "9 ways" unless nine are there.
- Skip the AI title molds: "The Ultimate Guide to...," "Everything You Need to Know
  About...," "Unlocking the Power of...," "X Things You Need to Know," "Mastering the
  Art of...," "Why X Is the Future of Y," "A Deep Dive Into..."
- Drop empty superlatives ("the best way," "the only X you'll ever need," "the secret
  to") and filler words ("really," "actually," "simply," "just").

## Introductions

- Short: roughly 3 to 5 sentences and under 150 words, in two or three brief
  paragraphs. Never one dense block.
- Hook, then context, then a turn into the body. Lead with the reader's problem and
  give the bottom line in the first few sentences, since many readers (and answer
  engines) take only the opening.
- Skip the stock openers: "In today's fast-paced world," "It's no secret that," "In an
  era of," "In the ever-changing landscape of," "Whether you're a beginner or a pro."
  No dictionary definitions. No "In this post, you'll learn: 1, 2, 3."

## Conclusions

- Its own H2, the last one, under a heading that says something. If the outline
  calls for a conclusion, write one; never drop it.
- Make it substantive: a clear next step, what the reader can now do, or the caveat
  that matters most. Don't relist every point, and don't restate the opening (see
  the tidy, self-announcing post above).
- Add a CTA only if it fits. For an explainer or analysis, skip it.
- Avoid the announced endings above; deliver the last thought directly.

## FAQ (optional)

- Add one only when readers still have real questions the body didn't answer. Don't
  repeat body content as questions.
- 3 to 5 questions a real person would type into Google or an AI assistant.
- Each question is an H3; answers run 2 to 4 sentences, answer first.
- Don't restate the question inside the answer, and don't open every one with "Yes" or
  "No." Vary them. No rules between questions.

## Links

- Markdown with descriptive anchor text, 2 to 6 words. Never a bare URL on its own
  line (except a video URL placed on purpose to auto-embed), never "click here,"
  "read more," "learn more," or "this article."
- Link only where it helps the reader act on the sentence they're reading. Editorial
  value first. Prefer a deep page over a homepage.
- One link per destination, absolute URLs, roughly one internal link per 300 words.
- Only link URLs you were given or verified. Never guess a path.

## Quick self-check before shipping

Run this on every draft. It takes a minute and catches most of the damage.

1. Read the first and last paragraphs together. If the close recaps, rewrite it to
   end on something new; keep the conclusion itself. Cut a roadmap paragraph, and
   cut a summary block unless it's the one a long reference post earned.
2. Search the text for "—" (em dash), "–", "→", "serves as", "it's not",
   "isn't just", "here's the", "let's dive", "in this post", "gone are the days",
   "in conclusion", "key takeaways", "delve", "landscape", "moreover",
   "furthermore", "studies show", "experts say", "**" at the start of a list item.
   Fix every hard-rule hit and every "gone are the days" or "in this post" hit. For
   the rest, fix repeats. A "key takeaways" hit is fine if it's the post's one
   permitted summary.
3. Read any three sentences in a row out loud. Different opening words? Different
   lengths? Any metaphor where a plain phrase would do?
4. Check every number, name, quote, and claim of experience against your source
   material. If you can't point to where it came from, it goes. When you edit an
   author's draft, their own stated facts count as source: keep them and flag any
   worth checking.
5. Could a sentence sit unchanged in a competitor's post on the same topic? Sharpen it
   or cut it.
6. Did you make each point once, or dress the same one up five times?

Run it once. A second pass hunting only for tells tends to make text worse: it
removes the author's voice and replaces one pattern with another.
