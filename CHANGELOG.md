# Changelog

What changed in the Decision Wizard and the d-wizard skill, newest first. The wizard and the skill keep their own version numbers. 

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
