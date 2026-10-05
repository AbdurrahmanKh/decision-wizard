# Changelog

What changed in the Decision Wizard and the d-wizard skill, newest first. The wizard and the skill keep their own version numbers.

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
