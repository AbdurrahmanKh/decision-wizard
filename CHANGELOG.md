# Changelog

What changed in the Decision Wizard and the d-wizard skill, newest first. The wizard and the skill keep their own version numbers. 

## Skill 0.11.0, 13 November 2026

### Added

- Skill: `scripts/validate_round.py` checks a round before Claude sends it: unique ids, titles that aren't questions, questions that end with a question mark, unique option labels, at most three cards, recommendations that name a real option or value, follow-ups whose `when` names a real option, table rows as wide as their columns, `needs_wizard` high enough for the question types, and no em or en dashes. It prints `ok`, or one problem per line, and skips brainstorms.
- Skill: `scripts/read_answers.py` prints a round's answers one line per id, with notes, rows, and follow-ups under it. Given a round with no answers yet, it reads the newest saved answers with the same title from the same folder. `--full` adds each question and the text of a picked card. Claude reads answers through it instead of reading the whole round file again.

### Changed

- Skill: `wizard-rounds/` stays out of git through its own `.gitignore` holding `*`. Claude no longer edits the project's `.gitignore` for it.
- Skill: a session working in a git worktree writes rounds to the main checkout's `wizard-rounds/`, since a worktree is deleted once its work is done. Before a new round, Claude looks there for earlier rounds on the same topic.

## Wizard 0.11.7, 11 November 2026

### Added

- Wizard: every answer, and every answer of a follow-up, has a small pen at its edge. A click on the pen picks that answer, stays on the question, and puts you in its note box. Ctrl+Enter or Cmd+Enter in a note box records the note and moves on, the way picking does. The pen turns gold on the picked answer once it has a note.
- Wizard: Shift with a number key does the same as the pen: Shift+2 picks the second answer and opens its note. The number keys alone still pick and move on.

### Fixed

- Wizard: number keys pick again after a click on an empty part of the page, such as the space beside a card. The click put the focus on the page's main area, where the keys didn't count.
- Wizard: typing a note no longer replaces the pen on the Add a note button with the word Note.

## Wizard 0.11.6, 1 November 2026

### Added

- Wizard: in Options, a companion's tile rocks on its feet while the mouse rests on it: a lean to the right, then left and right in turn, 12 degrees each way, about 1.4 seconds a full rock. It keeps rocking while the mouse stays, even after a click picks it, and eases back to standing when the mouse leaves. The None tile stays still, a tap on a touch screen doesn't start it, and with your system's reduce motion setting on, no tile rocks.

## Wizard 0.11.5 and skill 0.10.1, 30 October 2026

### Changed

- Wizard: Options is five sections that fold: Companion, Look, Answering (Wizard recommendations, where the context shows, and Number keys pick answers), Time (the round timer and the time estimate), and App and data (Install, Back up all rounds first, and Clear everything). A click on a section's heading folds or opens it. The gold dash before the heading turns into a plus while the section is folded, and a folded heading shows its settings after its name, such as "Dark, Normal". Each section stays as you left it in this browser; the first time, only Companion is open.
- Wizard: every On and Off pair in Options is one switch.
- Wizard: a note that explains a setting waits behind a small i after the setting's name, and opens in place under it. A companions folder that can't be read, or that the browser blocks, still says so in view.
- Wizard: the companion tiles are all picture. Five share a row, each companion fills its tile, and its name sits on a soft fade over its feet. None stays a tile. Add, and Create, which was Build, sit in the Companions folder row.
- Wizard: Stats is a small chart beside the close button at the top of Options. It opens your counts in a popup over the panel, and the Show stats button is gone.
- Wizard: while the Companion section is folded, your companion answers a change in Options from its place beside the cards instead of from its tile.
- Skill: the companion guide names Create, next to Add, where it named Build.

### Fixed

- Wizard: Clear everything now also puts Number keys, where the context shows, and the time estimate back to how they start. Before, they kept your old choices until the page was reloaded, and any change in Options saved them again.

## Wizard 0.11.4, 28 October 2026

### Changed

- Wizard: once your companion naps, it sleeps until you click it or its menu, or make a decision: an answer, a skip, a match in a bracket, or a choice in a brainstorm. Moving the pointer, scrolling, keys, and clicks anywhere else leave it asleep, where in 0.11.3 any of them woke it. While it sleeps it says nothing, and the round's clock waits with it: the time reads "Paused while Quill naps". A round that opens during the nap gets its greeting when your companion wakes. With no companion, coming back still starts the clock again.
- Wizard: on a grouped card, clicking your companion brings the grid up a moment later, and only while a row is still open. After the last row, the circles fade sooner, and a click doesn't bring them back.

### Fixed

- Wizard: clicking your companion fast for the dance showed the grid in its thought bubble. The dance now hides any thought.
- Wizard: the thought bubble's trail ran off to the right of your companion's head. It now curves down into it.
- Wizard: on a screen wider than 1500 px, your companion stood left of the middle of its column, so its bubbles and the speech bubble's pointer missed it. It now stands in the middle, under them.

## Wizard 0.11.3, 27 October 2026

### Added

- Wizard: your companion's lines are laid out to read at a glance. Each line is split into its sentences and shows in one of the shapes that fit it: as it is, or one sentence a line, and on a wide screen, now and then, with its number up in a thought bubble over your companion too. The shape changes from one line to the next. A long line arrives a piece at a time, 0.8 seconds apart, like chat messages; with your system's reduce motion setting on, it shows at once.
- Wizard: what the wizard fills into a line shows in bold, in your companion's color, with a small icon, the size of the words around it: the decisions ahead (a stack of cards), the time a round may take (a clock whose slice shows the minutes) and the time it took (a stopwatch), answers you picked (a check mark) and wrote (a quill), questions still open (an open circle), rounds finished (a trophy), decisions today (a sun), and answers about to be cleared (a warning sign). Counts are digits that stay on one line with their word, "7 decisions", even at the start of a sentence, and the estimate reads "9 min".
- Wizard: those words are green for Quill and slate for Swoop. A companion you made takes the strongest color in its idle picture, or its black, white, or grey when it has no real color, darkened until it reads on the bubble.
- Wizard: the estimate learns your pace. The time you spend on each question is kept, leaving out the minutes before a nap, and once you've finished three rounds the estimate follows your own seconds for each kind of question. Time estimate, in Options, has Follow my pace, on to start with, and Seconds for a plain question, to set your own; the other kinds keep their share of it. Before it has learned, the estimate starts from a real pace, about twice what it used to count. Quill and Swoop say when the estimate is yours: "About 12 minutes, at your pace." Backups keep the time per question.
- Wizard: Quill and Swoop have a line for a pick other than the one with the wizard hat, at most once every five minutes: "Ignoring my recommendation again. Noted."
- Wizard: on a number question, your companion thinks of the value in a thought bubble as you move the slider. The thought bubble floats over its head on a wide screen, and beside it under 1440 px.
- Wizard: in a bracket, each option knocked out goes with a line of its own, its name struck through: "Pears is gone." The next match's line replaces it.
- Wizard: on a grouped card, your companion's thought bubble holds a grid of faint circles, one a row, pale yellow while open and pale green once answered, filling in as you go. It comes up once you answer a row on a card of more than five, or when you click your companion on any grouped card, stays beside its lines until you leave the card, and fades a moment after the last row. A long card's circles are smaller, so the grid keeps its size. On a narrow screen it shows for a moment after each row.
- Wizard: a writing pose. Quill and Swoop take it while you type an answer of your own, a note, or an idea in a brainstorm, and go back once you stop. A companion you build can have one; without it, it stays as it is.
- Wizard: when your companion suggests calling another one in, that one peeks into the bubble, up over its edge and back, then settles. Call it in, and the one leaving waves goodbye as the new one steps up.
- Wizard: the builder has the new moments (Estimate, your pace; Against the hat; Knockout) and the writing pose among the pictures. Create with Claude still asks for the 14 poses.

### Changed

- Wizard: the bubble's words are aligned left everywhere, beside the cards and in the side column, where they were centered.
- Wizard: a line stays up 6 to 11 seconds by its length, where it was 4 to 9, and 13 with a button. A line waiting its turn is dropped after 45 seconds instead of 20, so longer lines don't push others out.
- Wizard: a remark that started on one question finishes after you move on, and what the next question brings waits for it: a grouped card's line comes after the remark, and after any line about your pick. Only the nudge to skip a question you've just answered is still dropped.
- Wizard: your companion naps after 3 minutes away instead of 4, with the yawn half a minute before.
- Wizard: the line for an answer the moment its question showed now comes within 6 seconds of it, where it was 2.

### Fixed

- Wizard: anything that says you're back wakes your companion from a nap: moving the pointer, the wheel, a key, a click or tap anywhere, or coming back to the window. Before, only a click or a key did, so the round's clock could stay paused while you read.

## Wizard 0.11.2, 24 October 2026

### Added

- Wizard: a `web+dwizard:` link opens the installed app from any browser or app, since a link clicked in one browser can't reach an app installed from another. The app registers the link type with the system (`protocol_handlers` in the manifest). The link names a round by its file and title (`web+dwizard:open/` and base64url JSON), and the wizard opens it from a connected folder that holds its file, else from its list, else says which folder to open once, or asks to be allowed into one it knows. Nullovation City's Wizard it opens rounds this way.

## Wizard 0.11.1, 24 October 2026

### Added

- Wizard: a link can open a round. The wizard's address with `#open=` and the round after it, as base64url JSON with `file`, `round` and `answers`, opens that round whatever was on screen: one already in the list opens with its answers, a changed version replaces it as Load would, and a new one comes in with the answers sent along. A round that names no folder saves into a connected folder that holds its file. Nullovation City's Wizard it opens its rounds this way.

### Changed

- Wizard: the installed app keeps to one window. In Chrome and Edge a link to the wizard opens in the app's open window, which gets it through its launch queue (`launch_handler`, `focus-existing`, in the manifest).

## Wizard 0.11.0 and skill 0.10.0, 23 October 2026

### Added

- Wizard: round 1's questions are a group chat on a phone. Each hat asks its question, then the sparks come, one at a time; answer in the box and the next hat types for a moment before it asks, or skip with Next question. Back goes to an earlier question, and the Left and Right arrow keys step through them. Your answers show in the chat with your companion's face, or You with no companion, each with Edit and Delete.
- Wizard: each idea on the council is a group chat too. The hats speak in turn, Cap last, and the next one types while you read; the arrow on the device names who's next. The buttons sit under the message showing, and fold into what you did once you move on. Past the last hat, the arrow carries on to the next idea, and Back from the first comment goes to the idea before.
- Wizard: the idea has its own card above the chat, with Rewrite, the ideas a merged one came from, and a cross to kill it that outlines the idea in red. A change you take, and your answer to a hat's question with the question beside it, stick onto the idea as strips of torn paper in the hat's color, light or dark with the theme, each with Edit and a cross to take it off.
- Wizard: round 2's aims card lists what else you told the hats: your round 1 answers that weren't ideas, each with the question it answered. A format change: round 2's `aims` can carry `said`.
- Skill: the test for an idea. A round 1 answer becomes an idea only when it names something that could be built or done; a goal goes to the aims, a concern to what to avoid, and anything else, such as a fact or a feeling, to `aims.said`, where extras can grow from it.

### Changed

- Wizard: an answer on the council moves the chat on to the next hat; taking a comment doesn't. Your companion says what you did in plain words ("Taking this as a change."), and a new idea or variant joins the new ideas below the chat. The box at the bottom writes a variant, or your answer once you press Answer it.
- Wizard: a comment counts as read once its message shows, and a hat with nothing to say stays quiet, greyed in the chat's header, instead of saying a built-in line.
- Wizard: Cap's recap of round 1 lists every question with your answers, or Skipped, then the suggestions you kept, hat by hat.
- Wizard: round 1's plan reads Questions, Suggestions, Recap, the list beside the cards groups the hats' questions under Questions, and the extras' own line, when Claude writes none, says "the hats had a few more ideas".
- Wizard: what you type in round 1's box stays there while you move about round 1's questions, and is kept as an answer to the question showing when you leave them.
- Wizard: the round table, with its seats, bubbles, and gold marks, is gone, and so are the council setting in Options (Round table or In a row) and the built-in lines for a hat with nothing to say.
- Skill: sparks are always questions; round 1 is described as questions the user answers or skips; the council's comments are written in the order the hats should speak, Blue last; and `read` means the hat's comments reached the user. `needs_wizard` is `"0.11.0"` on round 2.
- Skill: `references/brainstorms.md` no longer describes the wizard's screens, only what the user can do, so a new layout never needs a skill update.

## Wizard 0.10.1 and skill 0.9.1, 21 October 2026

### Added

- Wizard: the Context panel folds. Hide, on its header, folds it to one bar on that question, and Show brings it back. Every new question opens with its context showing, and a question you folded stays folded while the page is open.
- Wizard: a Context card in Options, with Before the answers, the default, or After the answers, where 0.10.0 put it.

### Changed

- Wizard: a question's context now sits between the question and its answers, so the framing, quotes, and notes come before the options. This holds for every kind of question and for follow-ups, each with its own context. Brainstorm cards keep their context where it was.
- Skill: no longer describes where the wizard shows things (the context, the title, the question, a recommendation's reason), so a change to the wizard's layout never needs a skill update. Rounds and answers are unchanged.

## Wizard 0.10.0 and skill 0.9.0, 17 October 2026

### Added

- Wizard: on the council, take a comment as a new idea, as before, or as a change to the idea. A change stays with the idea, under it in Changes you took, and goes back to Claude with it.
- Wizard: Answer it, under a comment that ends on a question. Your answer becomes a change to the idea, with the question it answers.
- Wizard: Rewrite, on the idea. Its words open in a box with the changes you took beside them; once saved, what you changed is marked against the original, struck words gone and highlighted words new. Back to the original undoes it.
- Wizard: Use as the idea's words, on Blue's "Closer to your goal:" version, which takes it whole as the idea's new words, marked the same way.
- Wizard: a hat can say up to four things on one idea. Its seat shows how many, and its bubble lists them, each with its own buttons.
- Wizard: merged ideas. Claude can merge cards from round 1 into one idea, and Show the ideas it came from lists them.
- Wizard: Leave it to Claude, on the order card once you've moved something, gives the order back.
- Skill: round 2 merges cards that belong together into one idea, keeping every card it came from; a hat can say several things on one idea; and the skill reads the changes, answers, and rewrites that come back, taking each idea as you left it.

### Changed

- Wizard: each hat talks in its own color, in its card's line, its sparks, and its council bubble, in place of the plain white bubble.
- Wizard: the order card says it starts in the council's order, and that Claude orders the ideas when you leave it as it is.
- Skill: round 2 needs wizard 0.10.0; round 1 still needs 0.9.0.
- Skill: after round 2, every card that survived counts as wanted, the hats' suggestions and extras included. The decision round asks only what your rewrites and answers leave open, and asks what only you know, such as which of your games, with a typed answer.

### Fixed

- Wizard: passing the order card no longer counts as setting the order. Before, Next or Finish there sent the order back as yours even when you hadn't moved anything.

## Skill 0.8.1, 17 October 2026

### Changed

- Skill: on the council, every hat hands you something to use on the idea, never a remark about it. Blue sharpens: written last, one line that starts "Closer to your goal:" with the idea changed to serve your goals better and the best of the other hats folded in, ready to take whole. White grounds: known pitfalls, technical, UX, or game design, that bear on the idea, saying where each is known from. Red names a feeling, then changes the idea to cause it, for the person who'll use the thing. Yellow grows the idea, or names the next idea it unlocks. Black's cracks and Green's twists stay as they were.
- Skill: a comment that could sit under any other idea unchanged isn't written. That hat stays silent and says its own short line.
- Skill: before writing each round of a brainstorm, Claude searches the web for what's known about the topic, where web search is available, and White names where each fact was found.
- Skill: ordering what survives round 2 is up to you. The order card starts in the order Claude suggests; leave it as it is and Claude orders the ideas itself and starts the decision round from its own top, without asking you to rank anything.
- Skill: both brainstorm examples follow the new council and name White's sources.

## Wizard 0.9.1, 16 October 2026

### Changed

- Wizard: Sleep, with a Zzz, takes the place of Next open question in the companion's menu. It puts the companion to sleep right away, as a long time away does, and stops the round's clock until you wake it with a click or a key. While the companion sleeps, the menu leaves Sleep out. The question list beside the cards already jumps to any open question.

## Wizard 0.9.0 and skill 0.8.0, 14 October 2026

### Added

- Wizard: brainstorms in two rounds, replacing 0.8.0's one-file brainstorm. A brainstorm is for finding ideas; details and ways of doing them are left to rounds.
- Wizard: round 1 runs in three passes. Your turn: each hat asks one question and shows nothing else, and one box under the question drops each card into the grid below with Enter. Sparks: a hat's questions that might set off ideas, each with its own box, and a card written under a spark remembers it. Suggestions: your cards under the hat first, then up to four from the hat, with a box to add one more; Blue's are other paths to the same goal. Blue's recap shows what's standing, hat by hat, with counts.
- Wizard: kill replaces the star. Every card, yours and the hats', has a cross. A killed card crumples into a faceted paper ball and is tossed into the bin in the top bar, which shows the count and opens a panel listing every killed card with its hat and Restore. With reduced motion it fades instead. Your own cards can be edited too.
- Wizard: round 2. Blue opens on your aims, your goals and what you want to avoid, with the plan. Then the hats' extras, grouped by hat, to kill or keep: a kept extra comes to the council in the same round, a killed one never does. Then the council, one idea at a time, with the six hats around it: a gold mark on each hat with something to say, its comment in a bubble when you open it (hover or click), a green check once it has been open three seconds and counts as read, and Take it as an idea. A hat with nothing to say has no mark and says a short line of its own. Under the idea: Add a variant of your own, and Kill this idea. Last, your order: every idea that survived, with what you took or added, moved by its drag handle or its arrows.
- Wizard: nothing typed is lost. Text left in a box, or an edit left open, is kept as a card when you move to another card, however you get there.
- Wizard: a Brainstorms card in Options, with The council: Round table (the default, three hats on each side of the idea, and on a phone three above and three below) or In a row (under the idea).
- Wizard: what goes back to Claude: every card you wrote, by pass and by spark, every kill, the comments you read, what you took and added, and your order, with whether you set it.
- Skill: `references/brainstorms.md`, rewritten for the two rounds: the cast's jobs at each step, the spark rule (a spark names a direction, never the idea), writing round 1, writing round 2 from round 1's answers (your goals and concerns into the aims, every idea that survived as you wrote it, the extras, and the council, where White and Black end on a question and a hat with nothing to add stays silent), both rounds' answers, and what comes next. `references/example-brainstorm-round2.json` is a complete round 2.
- Skill: when a decision round comes back with a question left open and a note saying you're unsure, Claude offers a brainstorm on that one question, in one line.

### Changed

- Wizard: the hats' labels follow their new jobs: Blue the point, White realistic, Red human, Yellow the dream, Black caution, Green twists.
- Wizard: Load shows which round a brainstorm is ("Brainstorm, round 1") and counts cards seen. When a brainstorm has no tagline, the one under the title says which round it is. What the files look like, in Load, describes both rounds.
- Wizard: 0.8.0's brainstorms are retired. A file made for 0.8.0 no longer loads, and the wizard says why. One already in your list stays there, marked as made by an older wizard, with its answers ready to copy, and a backup holding one still restores it.
- Skill: `references/example-brainstorm.json` is now a round 1. Round 2 comes without asking once round 1 is back, and after round 2 the decision round names the brainstorm in its tagline and starts from the top of your order. The description and the compatibility line name wizard 0.9.0 for brainstorms.

## Wizard 0.8.0 and skill 0.7.0, 14 October 2026

### Added

- Wizard: brainstorms, a new kind of file. A brainstorm looks at one topic through the Six Thinking Hats, one card per hat. Blue opens with the focus, the plan, and the topic's context in full. White (facts), Red (feelings), Yellow (benefits), Black (caution), and Green (new ideas) follow in the order Claude picked, and Blue closes with what you starred and the next steps. Each card says what its hat's kind of thinking is.
- Wizard: the cast. A character wears each hat at the head of its card, with the hat's name first and the character's name beside it: Cap, the capybara (Blue), Tally, the owl (White), Ruby, the fox (Red), Sunny, the bee (Yellow), Pebble, the tortoise (Black), and Doodle, the chameleon (Green). Each says the line Claude wrote for it, and has three poses: speaking as its card opens, pleased when you star one of its ideas, and still.
- Wizard: on a hat's card, its ideas are sticky notes. Star what matters, add a note to any idea, and add ideas of your own: they start starred, up to 20 a hat, and Enter adds one while Shift+Enter starts a new line. When a hat asks you something, the answer box is on its card. Next marks the hat as seen; the plan on Blue's first card and the list beside the cards jump to any hat. Nothing is picked and nothing is recommended.
- Wizard: the brainstorm's summary shows what you starred and wrote under each hat, with the answers JSON. Everything goes back to Claude, the ideas you didn't star too.
- Wizard: brainstorms sit in Load with the rounds, marked with a hat and Brainstorm, with how many hats you've seen. They save, back up, restore, and work with project folders as rounds do, and files go out in the brainstorm's own form. A new version of a brainstorm keeps your stars and notes on ideas whose words didn't change, your own ideas, and your answers. What the files look like, in Load, describes a brainstorm.
- Skill: brainstorms. `references/brainstorms.md`, read only when a brainstorm is sent or answered, has the format, the cast and their voices, how to write each hat, how to deliver it, what comes back, and what to do next. `references/example-brainstorm.json` is a complete brainstorm.
- Skill: on a hard open question with no clear options yet, Claude offers a brainstorm in one line, and sends one only when you ask. After a brainstorm, Claude sums up what you starred and sends anything left to decide as a decision round.

### Changed

- Wizard: while a brainstorm is open, the companion keeps its faces but says nothing, so the hats do the talking. Brainstorms don't count in stats.
- Skill: the description covers brainstorms, and the compatibility line names wizard 0.8.0 for them.

### Fixed

- Wizard: on a phone, the question list could make the whole page scroll sideways. It now scrolls inside itself.

## Wizard 0.7.5, 13 October 2026

### Added

- Wizard: a Keys card in Options, with Number keys pick answers, On or Off. It's on from the first visit.
- Wizard: Skip to the question, a link at the top of the page that shows when you press Tab.

### Changed

- Wizard: on a screen under 1440 px wide, the companion no longer takes a row above the cards. Beside the question list it stands under the list, and stays in view as you scroll. On a narrower screen it stands beside the progress bar, and its lines show over the bar. The cards start 72 px higher, and over 100 px higher on a phone. The companion's menu opens below it, or above it where there's no room below.
- Wizard: focus follows your answers. After a pick, focus moves to the next question, or to the follow-up the pick opened. After a bracket pick it moves to the next match, and after the last one to the winner. Back, Skip, Next, Next open question, and the question list take focus to the question. Closing a popup, the custom answer, a notice, Options, or the builder gives focus back to where you were.
- Wizard: number keys pick only while you're on the question, never from the question list, the header, or the companion.
- Wizard: a number typed into a number question that the question doesn't allow moves to the nearest allowed value, and Enter records it only on a second press, once you've seen it.
- Wizard: in the builder, Start from has a Start from it button, so moving through the list copies nothing until you press it.
- Wizard: a companion line with a button, like Skip for now, stays while you hover it or the button has focus, and when the line ends its button goes with it. A toast stays while you hover it, and a longer message stays longer.
- Wizard: in the question list, an open question is a ring and an answered one a dot, so they differ by shape as well as colour.
- Wizard: on a phone, the round's title wraps instead of being cut off.
- Wizard: in Options, rows that need a companion, or speech bubbles, say so under their name instead of fading.

### Fixed

- Wizard: screen readers now hear the question as a heading, which answer is picked, which question a set of answers belongs to, which row a grouped-row button or note is for, the position of a ranked item after a move, a number with its unit, each bracket match and who beat whom, and the current question in the list with whether it's answered. Arabic and Hebrew text is marked with its language.
- Wizard: what changes out of sight is said once: a grouped row's answer and count, a new notice, a mood added in Create with Claude, and a number moved to an allowed value. The notices list is no longer read out in full on every change.
- Wizard: the context popup is named, keeps focus inside, and gives it back when it closes. The companion's menu opens with the arrow keys, has Home and End, reads the round's time, and, when it opened on hover, no longer takes keys from where you are.
- Wizard: contrast. Muted and amber text in the light theme, red buttons in the dark theme, placeholders, focus rings in the light theme and on the header, and the hat on a picked answer all reach WCAG AA.
- Wizard: the builder fits narrow screens and 400% zoom, and its moment descriptions wrap instead of being cut off. Two quotes side by side fit a 320 px screen.
- Wizard: a key wakes the napping companion, as a click does.

## Wizard 0.7.4 and skill 0.6.3, 13 October 2026

### Changed

- Wizard: the Create with Claude prompt is your description alone. It no longer adds the wizard's list of poses, moments, and line counts: the d-wizard skill knows all of that. The fold that showed it is gone, and what Copy prompt copies is exactly what the panel shows.
- Skill: `references/companions.md` describes the prompt as it now is: the description only, with everything else in that file.

## Wizard 0.7.3 and skill 0.6.2, 12 October 2026

### Added

- Wizard: **Create with Claude**, a button in the companion builder for a new companion. It opens a panel in the builder's place where you describe the companion: its name and the few words after it (shared with the builder), a title (a role or nickname for its lines), the language of its lines, its look, an art style with suggestions, details for any of its 14 poses, a sound it makes, and up to three moods, from suggestions or your own words. A prompt under the fields follows as you type. Copy prompt copies it with what the wizard needs, read from the wizard itself: the folder, the frame, the poses, and all 43 moments with their placeholders and line counts. A note says Claude needs the d-wizard skill 0.6.2 or later, and copying reminds you that you can add reference pictures. Back to the builder keeps what you wrote until the builder closes.
- Wizard: a companion's zip, dropped on the wizard or on the builder, is opened in the page and goes through the same question as a dropped folder. Only the one folder in the zip that holds a companion is read; files a computer can't name and the zip tools' own extras are left out; a zip with two companions, a password, damage, or more than 5 MB inside is turned away with the reason.
- Skill: `references/companions.md` reads the wizard's prompt (the prompt's own rules come first), uses the title, sound, mood, language, and any reference pictures, draws only original characters, writes the description into `companion.json` as `brief`, checks the folder before handing it over, and tells you to drop the zip on the wizard as it is.

### Changed

- Wizard: over the builder, the question to add a companion says it closes the builder, starts on neither button, and keeps the builder still while the companion is copied. A companion's folder dropped on the Create with Claude panel goes to that question, and pictures dropped on it go to the builder.
- Wizard: the drop overlay mentions a companion's zip.

## Wizard 0.7.2 and skill 0.6.1, 12 October 2026

### Added

- Wizard: the companion builder. **Build** in the Companion card of Options opens a workshop over the wizard for making a companion by hand: a tile for each of the 14 poses, where you choose or drop a picture and see which pose a missing one borrows; a stage that plays greet, pick, skip, milestone, warn, error, finish, the nap, and the dance with your pictures and lines; and every moment the companion can speak in, grouped, with a box per line, an example line, how many lines it needs, and the placeholders it can fill in as buttons. Start from copies Quill, Swoop, or one of your companions to begin with. The size against the 5 MB limit shows as you go, and Save says what's missing until the companion can be added. Save writes the folder into your companions folder and switches to it.
- Wizard: **Edit** beside each of your companions in the Companion card opens it in the builder. Save writes your changes back into its folder, leaves pictures you didn't change alone, and keeps any files and lines the builder doesn't show.
- Skill: `references/companions.md` gives the recommended number of lines for each moment (five for most, two for warn, one for speed, the recaps, open_go, and the Options moments), so a companion Claude makes has as many lines as each moment needs, and mentions Edit and Build when handing a companion over.

### Changed

- Wizard: closing the builder with changes not saved asks first. While the builder is open, the companion beside the cards keeps still and quiet, and pictures or a folder dropped on the page fill the poses their names match instead of adding a companion.

## Wizard 0.7.1, 12 October 2026

### Changed

- Wizard: Add, with no companions folder yet, asks only for the companions folder. If the folder you pick already holds companions, they show at once and that's it; only an empty folder goes on to ask for the companion to add.

### Fixed

- Wizard: picking your companions folder when asked for a companion's folder now says it's your companions folder, whose companions are already there, instead of saying it isn't a companion.

## Wizard 0.7.0 and skill 0.6.0, 9 October 2026

### Added

- Wizard: your own companions, in Chrome and Edge on a computer. Each is a folder of pictures, one per pose, with `companion.json` for its name and lines, inside one companions folder you pick once in Options. Add one with Add in the Companion card, or by dropping its folder on the wizard: the wizard shows it, asks first, then copies the folder in and switches to it. A folder you put there yourself joins by itself, and the folder is watched, so changes show within seconds. Remove deletes a companion's folder after asking.
- Wizard: a companion's poses can be drawings (SVG) or pictures (PNG, WebP, or GIF). Only the idle pose is needed; a missing pose borrows another. Small pixel art keeps its hard edges. Its lines can be in any language, and a right-to-left line reads right to left in the bubble.
- Wizard: a red notice for each folder in the companions folder that can't be added, saying why.
- Skill: `references/companions.md`, read only when you ask Claude for a companion: the poses, the frame, `companion.json`, every moment a companion can speak in and what it can fill in, and how the companion reaches you.

### Changed

- Wizard: the Companion card in Options shows each companion as a tile with its picture, with Add, None, and Hide for Quill and Swoop.
- Wizard: where folders can be opened, the drop overlay mentions a companion's folder.

## Wizard 0.6.3, 9 October 2026

### Added

- Wizard: new lines for Quill and Swoop. Most moments a companion speaks in a round now have five lines, and the companion picks one at random each time, never the same one twice in a row. A few moments keep fewer lines on purpose, such as the recaps after a round.

### Changed

- Wizard: when every question has an answer, the companion no longer says so. Go to first open shows "Nothing open. Every issue has an answer." under the summary's buttons, as it did with no companion, and Next open question in the companion's menu is greyed out.

## Wizard 0.6.2, 8 October 2026

### Changed

- Wizard: the questions the wizard asks you, like picking a project's folder or Clear everything, have a band across the top: green for a calm question, red for one that clears or replaces something. The band holds an icon, the title, and a Close button. Close answers nothing, as Escape does.
- Wizard: Options is in cards: Companion, Round timer, Recommendations, Look (theme and text size), Stats, App, and Saved data. The version sits in a footer that says options stay in this browser.
- Wizard: toasts and notices share one card look, with a tile for what each is: green for done or for news, gold for something that wants you, red for a problem. On a wide screen, notices sit above the list of questions instead of over the bottom of the page. On a narrower one they stay at the bottom, with toasts above them.

## Wizard 0.6.1 and skill 0.5.1, 7 October 2026

### Added

- Wizard: Open a project folder, in Load. Pick a project's `wizard-rounds/` folder and the wizard connects it, with no round loaded first, and opens the newest round in it that has no answers yet. The rounds in the folder name the project. A folder with no rounds from Claude Code, or a project's root with `wizard-rounds/` inside it, gets a short note and Pick again.

### Changed

- Skill: a project's `wizard-rounds/` folder is Claude Code's. Everywhere else, Claude included when it can reach your folders, a round comes to you as a file in the conversation, without a project or folder, and never lands in one of your folders.

### Fixed

- Wizard: a number pressed with Ctrl, Alt, or Cmd no longer picks an option. Ctrl+2, the browser's key for its second tab, used to record option 2 on the way.

## Wizard 0.6.0 and skill 0.5.0, 7 October 2026

### Added

- Wizard: project folders, for rounds Claude Code writes. A round can name its project and the folder its file is in. When one loads, the wizard says which project it's from and where it will save, and asks you to pick that folder once. It checks that the folder holds the round, then remembers it for the project. Chrome and Edge on a computer.
- Wizard: answers save themselves. With the folder connected, every answer and note is written into the round's file a moment later, in the saved-file form. A chip beside the section names the project and says when it last saved, and the summary says where the answers are. A round you haven't touched stays exactly as Claude wrote it.
- Wizard: new rounds open by themselves. A round that lands in a connected folder opens right away. While you're partway through another round it waits in Load instead, with a notice, a count on the Load button, and a New mark in the list. A corrected version of a round you already have arrives the same way, and the answers to questions that didn't change stay. When answers would be cleared, the new version waits for your look instead, with Review on the round, and nothing is saved over Claude's file until you've chosen.
- Wizard: Load lists the project folders the wizard has, each with its state, Allow when the browser wants your OK again, and Forget.
- Skill: a round written into a project's `wizard-rounds/` folder names the project and the folder, in `config.project` and `config.folder`, and Claude reads the answers from the round file once you say you've answered.

### Changed

- Wizard: a round's title is its identity within its project, so two projects can each have a round with the same title. Rounds with no project behave as before.
- Wizard: Save writes into the project's folder when the round's folder is connected.
- Wizard: with several wizard pages open, each page follows the rounds another one adds or deletes, and the answers given there to the round it has open.
- Skill: the message around a round can be three short sentences, and a round in a project folder is handed over without asking for a paste back.

### Fixed

- Wizard: a bracket you were partway through is kept when a new version of its round loads, as long as its question didn't change.
- Wizard: Clear everything no longer waits for other open wizard pages to let go of the stored file handles.

## Wizard 0.5.1, 6 October 2026

### Fixed

- The app's identity. The manifest's `id` was written as `./`, which browsers resolve against the site's root, so the installed app was identified as https://abdurrahmankh.github.io/ instead of the wizard's own address. The field is gone, and the identity is now the wizard's address. An app installed from 0.5.0 is a separate entry: uninstall it and install again.
- The service worker no longer refuses to install when one of the icons can't be fetched; only the page itself must be there.

## Wizard 0.5.0, 6 October 2026

### Added

- Back up and restore every round. Back up all rounds, in the Load panel and next to Clear everything in Options, writes every round in the browser with its answers to one file, each round in the saved-file form. Loading that file in any copy of the wizard adds the rounds that are missing, updates the ones the backup has a newer copy of, and asks before touching a round that changed here after the backup was made.
- The hosted wizard installs as an app, with its own window and icon, on computers and on Android. It opens offline, and whenever you're online it loads the newest version. Options gains an App section with an Install button where the browser offers one. This adds `manifest.webmanifest`, `sw.js`, and `icons/` next to `index.html`; local copies of the page work as before.

### Changed

- Dropping, choosing, or pasting a backup loads it like any other file.

### Fixed

- Clear everything also resets Wizard recommendations in the open page, not only after a reload.

## Wizard 0.4.0 and skill 0.4.0, 5 October 2026

### Added

- Wizard: ranking questions. Drag the rows into order by their handles, or move them with the up and down arrows on each row, by mouse, touch, or keyboard. Record this order saves the order, and the answer comes back as a list, best first.
- Wizard: number questions, with a minimum, a maximum, a step, and a unit. A slider shows where the value sits in the range, and a box beside it takes the exact value, which snaps to the range and the step. Record saves it, and the answer comes back as a number with its unit.
- Wizard: bracket questions, to pick one of 4 to 32 options. Options face off in knockout pairs, in the listed order, with a line such as "Match 3 of 7, round 2 of 3" and keys 1 and 2 to pick. After the last pick, the bracket stays on screen with the winner and every match, Next moves on, and Run it again starts it over. The answer comes back with every match.
- Wizard: recommendations on the new types. A ranking starts in Claude's order and a number on Claude's value, with the hat and the reason above them; on a bracket, the hat marks the recommended option in every match it plays.
- Skill: the three question types, with guidance on when to use each, and rounds name wizard 0.4.0 only when they use one of them.

## Wizard 0.3.0 and skill 0.3.0, 5 October 2026

### Added

- Wizard: a note on every question. A pen under the answers of every question and follow-up opens a note, so a pick can keep a condition ("B, but only for clans over 20 members"), and a question you leave open can still carry your view. Notes come back as `comment`, the field grouped rows already use, and show under their answers on the summary.
- Wizard: Wizard recommendations. When a round recommends an option, a small wizard hat marks it, with "I recommend this because..." under it when there's a reason. It shows on plain options, cards, follow-ups, and grouped rows, and picking still moves on. A Wizard recommendations switch in Options turns it off; it's on from the first visit.
- Wizard: rounds can name the wizard version they need, in `config.needs_wizard`, and the wizard keeps it with the round.
- Skill: recommendations, with `recommend` and `because` on questions, follow-ups, and grouped rows. Claude recommends wherever it has a view, with a reason whenever it has one.
- Skill: every round names the wizard version it needs, and the skill reads notes: a note next to a pick is part of the decision, and a note on an open question works like Discuss.

### Changed

- Wizard: grouped rows call their pen comments notes, to match.
- Wizard: a round is refused if its recommendation names an option it doesn't have.

### Fixed

- Wizard: opening a saved file whose only changes were follow-up answers now loads them, instead of saying the file matches what the browser already had.

## Wizard 0.2.1, 5 October 2026

### Changed

- Grouped questions keep their rows readable. When the answer buttons would squeeze a row's text into a narrow column, the buttons move under the text and the text gets the full width.
- Stats are back in Options, behind a Stats button: decisions made, decisions today, rounds finished, answers you wrote, and the fastest round, counted in this browser.

### Fixed

- A companion line about a question now ends when you leave that question, instead of playing on.

## Wizard 0.2.0 and skill 0.2.0, 5 October 2026

### Added

- Wizard: a question line. The title shows small, as the topic, and the question shows large under it. The sidebar and the summary keep the title, and the answers export carries the question after it.
- Wizard: a Context panel under the answers, with the framing, quote cards (two sources side by side), notes, links, and a button for each popup.
- Wizard: several popups per question, redesigned, with colored tables and quote, note, and code blocks.
- Skill: every question gets a plain question line, under a title that names the topic and is never a question.
- Skill: decisions stay decided. A pick, a typed answer, or a position stated in a comment is never asked again.

### Changed

- Skill: context stays in full. The skill judges what each question needs, keeps quotes that are important to understanding it, and splits longer material into labeled popups. Needs wizard 0.2.0.

### Fixed

- Wizard: number keys no longer answer behind an open popup, and a click outside closes it.
- Wizard: lines that open with an Arabic term in brackets, like "[القهوة]: most Qahwa wins", read in the right direction.

## Skill 0.1.1

### Added

- In Claude Code, opens the hosted wizard after the first round of a session.

## Skill 0.1.0

### Added

- Points anyone without a wizard to the hosted page.

## Wizard 0.1.0

### Added

- First stamped version: a library of rounds kept in the browser, Load and Save for round files, the Quill and Swoop companions, option cards, follow-up questions, a round timer, and light and dark themes.
