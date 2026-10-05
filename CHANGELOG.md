# Changelog

What changed in the Decision Wizard and the d-wizard skill, newest first. The wizard and the skill keep their own version numbers.

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
