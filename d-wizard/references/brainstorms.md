# Brainstorms

A brainstorm is for finding ideas on one open topic, not for settling details or ways of doing them: those are left to rounds. It runs through Edward de Bono's Six Thinking Hats, each worn by a character the wizard draws, and it always takes two rounds:

- **Round 1, questions, then ideas.** Each hat asks the user one question, and some hats then bring sparks: more questions that might set off ideas. The user answers what they like and skips the rest. Then every hat suggests ideas of its own, and the user kills any that miss.
- **Round 2, the council.** You write it from round 1's answers, sorting out which of them are ideas. The hats bring a few extras from what round 1 showed, and then every idea that survived, merged where cards belong together, comes before the council of all six hats, each handing the user something to use on it: a change, a known pitfall, a crack, or a twist. The user kills ideas, takes a hat's comment as a new idea or as a change to the idea, answers a hat's question, rewrites the idea in their own words, adds variants of their own, and can put what survives in order or leave the order to you.

After round 2 comes a decision round, starting from the top of that order. Every part serves one test: does it help generate more ideas?

Brainstorms need Decision Wizard 0.9.0 or later, and round 2 needs 0.11.0, which reads what the user said that wasn't an idea (`aims.said`); older wizards refuse it. So `needs_wizard` is `"0.9.0"` on round 1 and `"0.11.0"` on round 2. An older wizard can't open one, so point the user to https://abdurrahmankh.github.io/decision-wizard/ if theirs says the file isn't a round or asks for a newer wizard. Wizard 0.9.0 replaced the one-file brainstorms of 0.8.0 (a `hats` list) and refuses them, so never write that form.

## When

Send a brainstorm only when the user asks for one. When a hard open question has no clear options yet, so a round would only guess at them, offer one in a single line and wait. When round 1's answers come back, write round 2 without asking: two rounds is the design. When round 2's answers come back, the next step is usually a decision round.

## The cast

The wizard draws the six characters, gives each its name and label, and has each hat's question built in for round 1. You write every other word they say, fresh for each brainstorm, in that character's voice.

| Hat | Character | Label | Voice |
|---|---|---|---|
| Blue | Cap, the capybara | The point | Calm and unhurried; frames the question, keeps the order, and sums up |
| White | Tally, the owl | Realistic | Calm and exact; says what we know, what we don't, and where a number came from |
| Red | Ruby, the fox | Human | Warm and blunt; says how it feels, with no reasons needed |
| Yellow | Sunny, the bee | The dream | Bright and busy; finds what's good and how far it could go |
| Black | Pebble, the tortoise | Caution | Careful and dry; looks for the cracks and always gives the reason |
| Green | Doodle, the chameleon | Twists | Playful and odd; turns the question sideways and tries another way in |

What each hat does at each step:

| Hat | Asks in round 1 (built in) | Suggests in round 1 | Says on the council |
|---|---|---|---|
| Blue | "Where is this going, and what are its main goals?" | Other paths: reaching the goal through another feature entirely | Sharpens: the idea changed so it serves the core better, with the best of what the other hats said folded in |
| White | "What's the smallest version of this that would already be worth having?" | Realistic additions from what is known: facts that lead to new ideas, quick wins | Grounds: known pitfalls, technical, UX, or game design, from research, each with where it's known from |
| Red | "What excites you most about this?" | More human, engaging, and emotional versions: a plain tool made beautiful, a chore made warm | Humanizes or stirs: names a feeling, then changes the idea to cause it, for the person who'll use the thing |
| Yellow | "If you imagine it as wild as you can, how does it go?" | The dream: far ideas, hard to reach | Grows: the idea changed to be even more useful, further down its own road, or the next idea it unlocks |
| Black | "What could make this useless, or hurt and go badly?" | Ideas that avoid bad outcomes, long builds, or work nobody needs | Protects: the strongest way it could go wrong or not be worth it, even a rare one, a crack only this idea has |
| Green | "What's a twist on this that nobody would expect?" | Twists | Twists: the idea taken off its road, somewhere nobody expected, often more than one |

The first word of each council job is the hat's verb: what its comment does to the idea. The verbs are for you, to keep the hats apart; the user never sees them.

## Round 1

Round 1 asks before it suggests. First each hat asks its question, in the order of `hold`; then the hats with sparks ask them, in the order of `sparks`, each hat's in the order you list them. The user answers any question as often as they like, and skips any. Then each hat suggests its ideas, in the order of `suggest`, and the user kills any that miss and can add ideas of their own beside them. The wizard ends round 1 on Blue's recap, which it builds by itself.

```json
{
  "config": { "title": "Steam Handheld, Brainstorm 1", "tagline": "Round 1: your ideas first", "product": "Handheld", "project": "Handheld", "kind": "brainstorm", "round": 1, "needs_wizard": "0.9.0" },
  "topic": { "title": "Steam games on my handheld", "question": "What could get my Steam games onto my handheld?", "context": "..." },
  "hold": [
    { "hat": "blue" }, { "hat": "white" }, { "hat": "red" }, { "hat": "yellow" }, { "hat": "black" }, { "hat": "green" }
  ],
  "sparks": [
    { "hat": "yellow", "line": "Two to get you buzzing.", "sparks": [ { "id": "s3", "text": "Does the game have to run on the handheld at all?" }, { "id": "s4", "text": "What would you play if the battery never ran out?" } ] }
  ],
  "suggest": [
    { "hat": "white", "line": "Four within reach, from what we know.", "ideas": [ { "id": "w1", "text": "Start with games that already have a Linux build: no port needed." } ] },
    { "hat": "red", "line": "...", "ideas": [ ] },
    { "hat": "yellow", "line": "...", "ideas": [ ] },
    { "hat": "black", "line": "...", "ideas": [ ] },
    { "hat": "green", "line": "...", "ideas": [ ] },
    { "hat": "blue", "line": "Two other paths to the same place.", "ideas": [ { "id": "b1", "text": "Don't port at all: stream from the PC and spend the effort on the controls." } ] }
  ],
  "recap": { "line": "That's round 1. Send it back, and round 2 brings the council." }
}
```

For a complete round 1, read `example-brainstorm.json` next to this file.

`config` works as in a round: `kind` is always `"brainstorm"`, `round` is `1`, `needs_wizard` is `"0.9.0"`, `project` goes on every brainstorm, and `folder` on a brainstorm Claude Code writes into a project's `wizard-rounds/` folder, exactly as for a round.

`topic` is the one subject of the whole brainstorm, and both rounds carry the same one:

| Field | Required | What it does |
|---|---|---|
| title | yes | The topic as a short label, never a question |
| question | yes | The open question, in plain words, ending with a question mark |
| context, detail, links, extra | no | As in a round. Never cut context to make it shorter, and quote only what is important to understanding the topic |

The three lists:

| List | Shape | What goes in it |
|---|---|---|
| hold | Exactly six entries, `{"hat":"blue"}` first, then the other five once each, in the order you pick | Each entry can carry a `question`. Leave it out and the wizard asks the hat's own question from the table above. If you write one, keep what it asks and only name the topic: "What excites you most about playing your Steam games on the handheld?". Never give a hold entry a line: the hat only asks |
| sparks | Optional, one entry at most per hat, only for hats with a spark worth having | `line` (optional): what the hat says before its first spark. `question` (optional): names the entry in the answers, "What do these set off?" when left out. `sparks`: 1 to 3, each `{"id":"s1","text":"..."}` |
| suggest | Exactly six entries, each hat once, in the order you pick, with `{"hat":"blue"}` last | `line` (required): what the hat says as it suggests. `question` (optional): the hat's question as it suggests, its own when left out ("What's within reach?", "How could it feel more human?", "How far could it go?", "What would keep it out of trouble?", "What twist could feed it?", and for Blue "What other path could get you there?"). `ideas`: 0 to 4, each `{"id":"w1","text":"...","why":"..."}`; `why` is optional and short, such as where a fact came from |

`recap` is optional: `{"line":"..."}`, Blue's line as round 1 ends.

Ids are short, use only letters, digits, `-`, and `_`, and are unique across the file: a letter for the kind and a number (`s1` for sparks, `w1`, `r1`, `y1`, `k1`, `g1`, `b1` for suggestions). Ids like `u1` are kept for the user's own answers and ideas, and the wizard refuses them.

### Writing round 1

- **One topic.** A brainstorm explores one open question. Several questions are several brainstorms, or a round.
- **You write before the user answers.** The whole of round 1 goes out at once, so your sparks and suggestions can't react to the user's answers: write them to stand on the topic alone.
- **The spark rule.** A spark is a question the user can answer. It names a direction, never the idea itself: if it could be built, it's a suggestion. "Does the game have to run on the handheld at all?" is a spark; "Stream your games from the PC" is a suggestion. Not every hat brings sparks: pick the hats where a nudge would help on this topic, up to three sparks each, and when a hat brings more than one, start calm and get wilder.
- **Suggestions follow the hat's job.** Up to 4 a hat, fewer when fewer are strong. Each is one sentence that stands alone, read days later with no chat history. Blue's are other paths to the same goal, never a summary.
- **Every hat speaks in its own voice.** A suggest line is one or two sentences in the character's voice, and so is a spark line when you give one.
- **Facts are real,** whichever hat states them. White's suggestions come from your research (see Both rounds), the conversation, or the files, with `why` naming where each was found when it isn't common knowledge. Never invent a number, and don't state as a rule what is only often true.
- **No recommendations.** No hat argues for an outcome. Every suggestion stays unless the user kills it.

## Round 2

Write round 2 from round 1's answers. Its parts, in the order the user meets them:

1. **Aims:** Blue opens on the user's goals, on what they want to avoid, and on what else they told the hats, as the measure for every idea.
2. **Extras:** new ideas from the hats. The user kills any that miss; a kept extra comes before the council in this same round, and a killed one never does.
3. **The council:** each idea, in the order you wrote them, then each kept extra, before the six hats. The hats speak on it in the order of its `council` list, and a hat left out says nothing on that idea. The user can take any comment as a new idea of theirs (it goes to the order) or as a change to this idea (it stays with the idea), and answer a comment that ends on a question; Blue's "Closer to your goal:" version can also become the idea's words. The user can also rewrite the idea in their own words, add variants of their own, or kill the idea.
4. **Your order:** every idea that survived, with what the user took or added, for them to put in order. It starts in the order you wrote the ideas, so leaving it untouched hands the ordering to you. Nothing the user adds in round 2 goes to a council: there is no round 3.

```json
{
  "config": { "title": "Steam Handheld, Brainstorm 1, Round 2", "tagline": "From Steam Handheld, Brainstorm 1", "product": "Handheld", "project": "Handheld", "kind": "brainstorm", "round": 2, "needs_wizard": "0.11.0" },
  "topic": { "title": "Steam games on my handheld", "question": "What could get my Steam games onto my handheld?", "context": "..." },
  "aims": {
    "line": "Round 2. The hats have a few more ideas first, then the council takes your ideas one at a time.",
    "goals": [ "Play my whole Steam library away from my desk." ],
    "avoid": [ "Hours of setup for games that run badly." ],
    "said": [ { "hat": "red", "question": "What excites you most about playing your Steam games on the handheld?", "answer": "Playing in bed without my PC on." } ]
  },
  "extras": {
    "line": "From what you wrote, the hats had a few more ideas. Kill any that miss.",
    "ideas": [
      { "id": "x1", "hat": "red", "text": "A cosy mode: dim screen, quiet fans, one game you can play half asleep.", "why": "From your \"Playing in bed without my PC on\".",
        "council": [ { "hat": "black", "say": "A dim screen hides small text in some games. Which games would it suit?" } ] }
    ]
  },
  "ideas": [
    { "id": "i1", "text": "Stream games from my PC when it's on, and put the effort into the controls instead of porting.", "by": "merged", "hat": "yellow",
      "merged": [ { "text": "Stream games from my PC when it's on.", "by": "you", "hat": "yellow", "from": "From Yellow's spark: Does the game have to run on the handheld at all?" },
                  { "text": "Don't port at all: stream from the PC and spend the effort on the controls.", "by": "blue", "hat": "blue" } ],
      "council": [ { "hat": "white", "say": "...?" }, { "hat": "black", "say": "...?" }, { "hat": "black", "say": "...?" }, { "hat": "green", "say": "..." }, { "hat": "blue", "say": "Closer to your goal: ..." } ] },
    { "id": "i2", "text": "Games with Steam Cloud already carry their saves between devices, so the handheld can pick up mid-game.", "by": "white", "hat": "white",
      "council": [ { "hat": "red", "say": "..." } ] }
  ],
  "order": { "line": "These made it through, in the order we'd take them. Move any you like, or leave it to Claude; the decision round starts from the top." }
}
```

For a complete round 2, read `example-brainstorm-round2.json` next to this file. It is cut to five ideas, one of them merged, and three extras to stay short; a real round 2 brings every idea that survived round 1, alone or merged.

| Field | Required | What it does |
|---|---|---|
| config | yes | As in round 1, with `round` set to `2`, `needs_wizard` set to `"0.11.0"`, its own title, and a tagline naming round 1: "From Steam Handheld, Brainstorm 1" |
| topic | yes | Round 1's topic. Keep it the same, adding to its context only a decision the user settled since round 1, or correcting a fact that has changed since, which you mention in one line when you deliver it |
| aims | yes | `line` (required): Blue's opening line. `goals` and `avoid`: lists of the user's own words, word for word. `said` (optional): the user's other answers, up to 60, each `{"hat":"red","question":"...","answer":"..."}`: the hat that asked, its question as the user saw it (the spark's words for an answer to a spark), and the answer word for word |
| extras | no | `line` (optional, Blue's) and `ideas`, each `{"id":"x1","hat":"red","text":"...","why":"...","council":[...]}`: `hat` is the hat that brings it, `why` (optional) what it grew from: the user's words, or a few words naming the answers. No fixed number; the wizard takes up to 40 |
| ideas | yes | 1 to 120, each `{"id":"i1","text":"...","by":"you","hat":"yellow","from":"...","council":[...]}`. `by` is `"you"` for the user's own idea, the hat that suggested it, or `"merged"` for an idea you merged from several. `hat` is the hat it came under in round 1; for a merged idea, the hat of the first of the user's own in it, or when it has none, the hat most of its parts came under, the first one's on a tie. `from` (optional) is one short line that goes with it: the spark it came from, for an idea the user gave in answer to a spark. Leave it out otherwise; a hat's idea without one reads "Suggested by White", and the user's has nothing |
| merged | on a merged idea, required | 2 to 12 ideas it came from, each `{"text":"...","by":"you","hat":"yellow","from":"..."}`, word for word: `by` and `hat` as on an idea, `from` when it had one |
| council | on each idea and extra, optional | Comments, each `{"hat":"white","say":"..."}`, in the order the hats speak, Blue last. A hat can say up to four things on one idea, each its own entry. A hat left out has nothing to say |
| order | no | `{"line":"..."}`, Blue's line as the order opens |

Ids follow round 1's rules, and are new for round 2: `i1` and on for ideas, `x1` and on for extras.

### Writing round 2

- **Sort the user's answers.** Read every answer the user gave and every idea they added, wherever, unless they killed it, and sort each by what it is. A goal is what the whole topic is for, often answering Blue: an answer that sets a standard for every idea, or for every part of the thing, saying what each must do, is a goal even if it could also be built. It goes into `aims.goals`. A concern is what must not happen, often answering Black: it goes into `aims.avoid`, whole, even when it carries a condition. An answer is an idea only when it names something that could be built or done, such as "a cheaper version that skips the port": one thing to build among others. Anything else, such as a fact, a feeling, or a plain "I don't know" ("Most of what I play is older indie games", "Playing in bed without my PC on"), is not an idea: it goes into `aims.said`, word for word with the question it answered, and you can grow extras from it. Goals, concerns, and what goes in `said` never come before the council, and they never take out an idea the user didn't kill, even one that pulls against them: the council can speak to the clash. `goals` can be empty; Blue then measures against the topic's question.
- **Every idea that survived reaches the council, alone or merged.** Each idea of the user's (`by: "you"`) and each suggestion they didn't kill (`by` its hat) either gets its own council turn word for word, or goes into one merged idea. Never reword or drop one outside a merge. An idea the user gave in answer to a spark gets `from` naming the whole spark: "From Yellow's spark: Does the game have to run on the handheld at all?". Suggestions the user never reached (their entry has `seen: false`) go too, since nothing killed them. A killed answer or suggestion never comes back: never merge one in.
- **Merge where it makes a more useful idea.** Ideas that say the same thing are one idea, even when one of them is a clear one of the user's, and so are ideas that fit together into one more useful than each alone. Write them as one sentence that keeps the user's words where they carry it (fix a plain typo, nothing more), with `by: "merged"`, `hat` as in the table above, and `merged` listing every idea it came from, word for word. Each goes into one merged idea at most. Don't merge ideas that pull different ways: a merge saves the user reading, never their meaning. An idea nothing else echoes stays alone, as written. The more ideas round 1 left, the more merging pays: fewer, stronger ideas keep the council worth reading and the order short.
- **Order the ideas** so related ones sit side by side, with the groups most likely to serve the user's goals first. The order starts in this order, so it is also the order you suggest: say so in the order's line. The wizard brings the extras after them.
- **Extras come from what round 1 showed** about the user: what they answered, the sparks that drew answers, what they said that wasn't an idea, and the directions they killed. Each steers clear of their concerns, and `why` quotes the answer it grew from when there is one, or the part of a long answer that matters, or names the answers briefly when it grew from several. Any hat can bring one, following its round 1 suggestion job. There's no quota: bring the ones worth a council turn.
- **Every comment hands the user something to use:** a change to the idea, a known pitfall, a crack, or a twist. Never a remark about the idea, a verdict such as "this fits the core", praise, or a list of benefits; a council of commenters is worth less than a decision round, which at least suggests changes. Each comment is one or two short sentences in the hat's voice, doing its job from the table above. A hat can say up to four things on one idea, each its own entry, when each passes the swap test on its own; Green most often, with more than one twist, and most hats say one thing or nothing. Write it as something the user could take as their own: the hat never says "I", and when an idea is about a hat, name that hat.
- **The swap test.** Before keeping a comment, check that it couldn't sit under another idea unchanged. If it could, it says nothing about this idea: leave that hat out. A hat speaks only when its comment would change what the user does with this idea, and a hat with nothing to add is simply left out, with no filler. Most ideas hear three or four hats, and all six is rare: fewer, stronger comments are what make the council worth going through.
- **The order they speak in.** Write each idea's comments in the order the hats should speak: the comment that changes the idea most first, a hat's several comments together, and Blue's last.
- **Blue sharpens, last.** Write Blue's comment once the others are written: one line that starts "Closer to your goal:" and gives the idea changed so it serves the core better, folding in the best of what the other hats said, so the user can take it whole. The opener is fixed; what follows is one changed idea, not a list of the others' points, and it passes the swap test like any comment. Use the words of the user's goals where they sharpen this idea, not as a phrase repeated on every idea, and never ask the user to choose again what a goal already says. Blue says one thing at most, and the user can take it as the idea's words, so write the whole idea after the opener, standing on its own. When Blue has nothing new to add, it stays silent.
- **White grounds, from research.** White brings the known pitfalls, technical, UX, or game design, whichever the topic calls for, that bear on this idea, from the research you did before writing (see Both rounds), and says in the comment where it's known from, as plainly as the fact needs: a field ("known from game streaming"), a named product, site, or rule, or a study by author and year when the fact rests on one. Pick the pitfalls someone building this idea would run into, not general findings about the field. White's pitfalls are known in a field; Black's cracks are the ones only this idea has, so the two never repeat each other.
- **Red humanizes or stirs.** Red names the feeling first, such as delight, pride, relief, or tension, then changes the idea to cause it, speaking for the person who'll use the thing: the moment they'd smile or give up, and the one change that would make them love it. It may bring a more human idea of the same kind instead. Red never only says how an idea feels.
- **Yellow grows, Green twists.** Yellow's comment is the idea changed to be even more useful, further down its own road, or the next idea it unlocks once it exists; never its benefits. Green takes the idea off its road. So every change has its own direction: Blue straighter, Yellow further, Green elsewhere, Red warmer.
- **White and Black end on a question** when there is one: a limit or a crack comes with what would get past it ("What would make it work on the go?"), so a problem can open an idea instead of only closing one. The user can answer it, and the answer comes back with the idea, so ask what only the user can answer.
- **Comments can become ideas or changes.** The user can take any comment as a new idea of theirs or as a change to this idea, so write each one to stand alone, read later without the idea above it.
- **Build on the user's ideas, never argue them away.** An idea of the user's that says what they want is still an idea before the council, and every comment on it adds to it: a change, a pitfall to get past, a twist in a new direction. No comment argues it away, and none leads back to an answer or suggestion the user killed.
- **Any hat can speak on any idea,** its own suggestions and the extras it brought included, always from its own job.
- **Facts are real, and no hat recommends.** As in round 1. A comment that states a fact beyond common knowledge says where it comes from, in the comment itself.

## Both rounds

- **Research first.** Before writing either round, search the web for what's known about the topic: the known pitfalls, technical, UX, or game design, whichever fit, and what others have already tried. For round 2, search too for what the surviving ideas need. White draws on it in both rounds and names where each fact was found: in `why` for a round 1 suggestion, in the comment itself on the council. Where web search isn't available, work from what you know, and say so in one of the sentences around the brainstorm.
- **Keep the user's words.** Their answers and ideas go into round 2 exactly as written.
- **Decisions stay decided.** A brainstorm never reopens a decision the user already made. State a settled decision in the topic's context as a fixed point instead.
- **Titles.** Round 1 names the brainstorm and its number ("Steam Handheld, Brainstorm 1"); round 2 adds ", Round 2". Reuse a title only to resend a corrected version, keeping unchanged entries identical so the user's work on them survives.
- Write in the user's working language. Titles are never questions; questions end with a question mark. No em dashes and no en dashes anywhere.

## Delivering it

Exactly as a round (see Delivering a round in SKILL.md), with the files named `<YYYY-MM-DD>-<name>-brainstorm<N>.json` for round 1 and `<YYYY-MM-DD>-<name>-brainstorm<N>-round2.json` for round 2: today's date, and the brainstorm's name from its title, lowercase with spaces and dots as hyphens ("Steam Handheld, Brainstorm 1" gives `steam-handheld`, "Brainstorm 2.0, Brainstorm 1" gives `brainstorm-2-0`). Round 2 keeps round 1's name and number. Surround it with as few short sentences as it needs: what Delivering a round asks for, and for round 2 also what round 1 left (see Acting on it) and any fact you corrected in the topic. Don't restate the brainstorm in prose.

## Consuming the answers

A brainstorm's answers carry `meta.kind = "brainstorm"` and `meta.round`. Every entry has `id`, `step`, `hat`, `issue` (the entry's title), `status: "brainstorm"`, and `seen`; all but the council's carry `question`. What the user wrote comes back in their words, without ids, and carries `killed` only when it's true. `topic` comes back with its title and question only: the context is in the brainstorm you wrote, and under `round` in a saved file. `meta.total` counts the entries and `meta.seen` those the user went through.

Round 1:

```json
{
  "meta": { "tool": "decision-wizard", "kind": "brainstorm", "round": 1, "wizard_version": "0.11.0", "wizard_title": "Steam Handheld, Brainstorm 1", "exported_at": "...", "total": 17, "seen": 17, "yours": 10, "killed": 3, "suggested": 15 },
  "topic": { "title": "Steam games on my handheld", "question": "What could get my Steam games onto my handheld?" },
  "answers": [
    { "id": "h-blue", "step": "hold", "hat": "blue", "issue": "Blue: your turn", "status": "brainstorm", "seen": true, "question": "Where is this going, and what are its main goals?",
      "yours": [ { "text": "Play my whole Steam library away from my desk." } ] },
    { "id": "h-black", "step": "hold", "hat": "black", "issue": "Black: your turn", "status": "brainstorm", "seen": true, "question": "What could make this useless, or hurt and go badly?",
      "yours": [ { "text": "Hours of setup for games that run badly." }, { "text": "Too slow to bother.", "killed": true } ] },
    { "id": "s-yellow", "step": "spark", "hat": "yellow", "issue": "Yellow: sparks", "status": "brainstorm", "seen": true, "question": "What do these set off?",
      "sparks": [ { "id": "s3", "text": "Does the game have to run on the handheld at all?", "yours": [ { "text": "Stream games from my PC when it's on." } ] },
                  { "id": "s4", "text": "What would you play if the battery never ran out?", "yours": [] } ] },
    { "id": "g-white", "step": "suggest", "hat": "white", "issue": "White: suggests", "status": "brainstorm", "seen": true, "question": "What's within reach?",
      "ideas": [ { "id": "w1", "text": "Start with games that already have a Linux build: no port needed.", "killed": false },
                 { "id": "w2", "text": "Check your library against a community list of games known to run, and start tonight.", "killed": true } ],
      "yours": [ { "text": "Try the three games I play most first." } ] },
    { "id": "recap", "step": "recap", "hat": "blue", "issue": "Blue: recap", "status": "brainstorm", "seen": true, "question": "What's standing after round 1?" }
  ]
}
```

- `step` is `hold`, `spark`, `suggest`, or `recap`, and the ids are `h-`, `s-`, and `g-` plus the hat. Blue's suggest entry is titled "Blue: other paths". Every hat has a hold and a suggest entry; only hats with sparks have a spark entry.
- `yours` is what the user wrote, in their words, and is authoritative: on a hold entry, their answers to the hat's question; on a spark entry, beside each spark, the answers it drew, and a `yours` beside the sparks, present only when there are any, holds answers tied to none; on a suggest entry, ideas they added beside the hat's. Each answer comes back on its own, and any of them may be an idea or not: sort them as Writing round 2 says. Answers from wizards before 0.11.0 are the same, though the user wrote them as cards.
- `killed: true` marks something the user killed, theirs or a hat's. Everything else is kept: there are no stars, and nothing not killed counts as standing.
- `meta.yours` counts what the user wrote, `meta.suggested` the hats' suggestions, and `meta.killed` the killed ones of both.

Round 2:

```json
{
  "meta": { "tool": "decision-wizard", "kind": "brainstorm", "round": 2, "wizard_version": "0.11.0", "wizard_title": "Steam Handheld, Brainstorm 1, Round 2", "exported_at": "...", "total": 12, "seen": 12, "yours": 2, "killed": 2, "ideas": 9 },
  "topic": { "title": "Steam games on my handheld", "question": "What could get my Steam games onto my handheld?" },
  "answers": [
    { "id": "aims", "step": "aims", "hat": "blue", "issue": "Blue: your aims", "status": "brainstorm", "seen": true, "question": "What could get my Steam games onto my handheld?" },
    { "id": "extras", "step": "extras", "hat": "blue", "issue": "Extras", "status": "brainstorm", "seen": true, "question": "Anything here worth keeping?",
      "ideas": [ { "id": "x1", "text": "A cosy mode: ...", "killed": false, "hat": "red" }, { "id": "x3", "text": "Your PC wakes itself ...", "killed": true, "hat": "green" } ] },
    { "id": "c-i1", "step": "council", "hat": "yellow", "issue": "Stream games from my PC when it's on, and put the effort ...", "status": "brainstorm", "seen": true,
      "idea": { "id": "i1", "text": "Stream games from my PC when it's on, and put the effort ...", "by": "merged", "hat": "yellow",
                "merged": [ { "text": "Stream games from my PC when it's on.", "by": "you", "hat": "yellow" }, { "text": "Don't port at all: ...", "by": "blue", "hat": "blue" } ] },
      "killed": false,
      "read": [ "blue", "white", "black" ],
      "taken": [ { "text": "Stream while the port downloads, then switch to the port when it's ready.", "hat": "green", "comment": "Stream while the port downloads, then switch to the port when it's ready." } ],
      "changes": [ { "text": "Plan for the train: download two games before leaving.", "hat": "black", "comment": "It all rests on the PC being on and the connection holding. What's the plan for a train ride?" } ],
      "answers": [ { "text": "Only the slow ones: strategy and card games.", "hat": "white", "question": "Known from game streaming: ... Which of your games are slow enough not to mind?" } ],
      "variants": [ { "text": "Stream at home, and download a port for the train." } ],
      "rewrite": { "text": "Stream my slower games with controls mapped for the handheld.", "original": "Stream games from my PC when it's on, and put the effort ..." } },
    { "id": "c-x3", "step": "council", "hat": "green", "issue": "Your PC wakes itself ...", "status": "brainstorm", "seen": false,
      "idea": { "id": "x3", "text": "Your PC wakes itself ...", "by": "green", "hat": "green", "extra": true }, "skipped": true, "killed": false, "read": [], "taken": [], "changes": [], "answers": [], "variants": [] },
    { "id": "order", "step": "order", "hat": "blue", "issue": "Blue: your order", "status": "brainstorm", "seen": true, "question": "Which ideas matter most?", "ranked": true,
      "order": [ { "text": "Stream my slower games with controls mapped for the handheld.", "by": "merged", "from": "round 1", "id": "i1", "rewritten": true, "changes": 2 },
                 { "text": "Get one game I own running, start to finish.", "by": "you", "from": "round 1", "id": "i3" },
                 { "text": "Stream while the port downloads, then switch to the port when it's ready.", "by": "you", "from": "taken from Green", "on": "i1" },
                 { "text": "Stream at home, and download a port for the train.", "by": "you", "from": "variant", "on": "i1" },
                 { "text": "Stream at home, and port only the games you take outside.", "by": "white", "from": "extra", "id": "x2" } ] }
  ]
}
```

- A council entry's id is `c-` plus the idea's id, and `idea.extra` marks an extra. `killed: true` means the user killed the idea; `skipped: true` means they killed the extra among the extras, so it never came before the council.
- `read` lists the hats whose comments reached the user. It says what they saw, not what they agreed with.
- `taken` are comments the user took as new ideas of their own, with the hat they came from; `variants` are ideas the user wrote on that idea. Both are the user's ideas, they go to the order, and each can carry `killed: true`.
- `changes` are comments the user took as changes to this idea, with their hat, and `answers` are the user's answers to a hat's question, with the `question` they answer. Both stay with the idea, never in the order on their own, and each can carry `killed: true`. They come from wizard 0.10.0.
- From 0.10.0, a taken comment and a change also carry `comment`: the hat's words it came from. `text` is the user's version, which they may have edited; when the two differ, `text` is what they want.
- `rewrite`, when present, is the idea in the user's own words, with your `original` beside it. `idea.merged` lists the ideas a merged idea came from.
- `order` is every idea that survived, best first, as the user left it: `from` is `round 1`, `extra`, `variant`, or `taken from` a hat, `id` names an idea or extra, and `on` names the idea a variant or taken comment came from. An idea the user rewrote carries `rewritten: true`, and its `text` is their words; `changes` counts the changes and answers that stay with it.
- **`ranked: false` means the user left the order to you.** From wizard 0.10.0, `ranked` is true only once the user moves something. Wizard 0.9 set it to true whenever the user went past the order, so for answers whose `meta.wizard_version` starts with 0.9, compare instead: the order starts with the ideas and extras in the order you wrote them, each followed by what the user took or added on it, in the order they did, and an order exactly like that is untouched, whatever `ranked` says.
- `meta.ideas` counts the council's ideas, `meta.yours` what the user took or added, and `meta.killed` everything killed: ideas, extras, and what the user wrote.

For both rounds:

- `seen: false` means the user never went through that entry; they may have jumped past it. What they did there still counts. Answers handed to you by the user are finished. Answers you read from a project's folder may not be: when the last entry (`recap` or `order`) isn't seen there and the user hasn't said they're done, ask whether they've finished before writing the next round.
- A file saved from the wizard carries the same `meta`, `topic`, and `answers`, plus the whole brainstorm under `round`, in the form you wrote, with every default question written in. A brainstorm in a project's `wizard-rounds/` folder is read back exactly as a round is.

## Acting on it

**After round 1:** write round 2 and deliver it. One sentence around it says what round 1 left: how many of the hats' questions and sparks the user answered, which sparks drew answers, how many of their answers became ideas, what they killed, and how many suggestions they never reached, if any. A brainstorm needs no report per id.

**After round 2:**

1. Take each idea as the user wants it: its words are their `rewrite` when there is one, otherwise yours, and its `changes` and `answers` stand with it either way, since a rewrite may fold some in and leave others beside it. A change they took is something they want; an answer is a position they stated, settled per Decisions stay decided. A hat's suggestion or an extra that survived is in, like the user's own ideas: they had every chance to kill it.
2. Sum it up in a few lines: the top three or four of the order, then counts of what they took and added (new ideas, changes, answers, variants, and rewrites, each by kind) and what they killed. Don't list the rest back. When the order is untouched, it's yours to set: weigh what survived against the user's aims and what they did on the council (what they took, added, and read), put the related ideas together, and say in one line that you ordered it.
3. If decisions remain, send a decision round, built from that order. It's named for the brainstorm: title "<name>, Round 1" ("Steam Handheld, Round 1"), file `<YYYY-MM-DD>-<name>-round1.json`, and a tagline that names the brainstorm ("From Steam Handheld, Brainstorm 1"). Its questions follow the order, top first, unless a later decision blocks an earlier one, and they ask only what's still open: the details and ways of doing that the brainstorm left to rounds.
   - Everything that survived is wanted: the user's own ideas, the comments they took, their variants, changes, answers, and rewrites, and the hats' suggestions and extras they didn't kill. Never ask whether they want one, or ask again what an answer or a rewrite settled; ask only what they leave open. A comment they took that ends on a question means they want that question answered: it becomes a question in the round, unless their rewrite or an answer already settles it.
   - When a detail depends on what only the user knows, such as which of their games, ask it with a typed answer (`customLabel` naming what to type) beside the routes you can offer.
   - Quote only the user's own words where they matter: their answers, ideas, variants, and rewrites, with the round they wrote them in as `src`: "Steam Handheld, Brainstorm 1" for round 1, "Steam Handheld, Brainstorm 1, Round 2" for what they wrote on the council. Hats' suggestions and council comments are your own writing, so they go in notes, never quotes, even ones the user took.
   - A question may touch the ground of a killed idea when a wanted one needs it, but never offers the killed idea back as an option.
   - Never ask the user to rank what survived: when they leave the order to you, ordering is yours.
   - The summary comes first, then the round with at most three short sentences of its own.
4. Killed ideas and skipped extras never come back, and a position the user wrote in an answer is settled, per Decisions stay decided.
5. If nothing remains to decide, say so after the summary. Neither round needs a report per id: the summary is the report.

A new angle on the topic is a new brainstorm with its own title, sent only when the user asks.

## Older brainstorms

Answers from a wizard 0.8.0 brainstorm have `meta.kind = "brainstorm"` and no `meta.round`, with an entry per hat whose ideas carry `starred`. Read them as they were meant: a star marks what mattered to the user, an idea without one was heard and not rejected, `yours` are the user's own ideas, `comment` is their note, and `answer` is their reply to a hat's `ask`. Never send that form again; to go further on its topic, offer a new brainstorm.
