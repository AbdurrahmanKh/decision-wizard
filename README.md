# Decision Wizard

Answer Claude's decision rounds one question at a time, then hand the answers back.

The Decision Wizard is a single web page that works with Claude's **d-wizard** skill. Claude writes your open decisions into a round file. You load it here and answer it. Claude then acts on each answer and reports where it landed.

**Open the wizard: https://AbdurrahmanKh.github.io/decision-wizard/**

## Install the skill

- **Claude:** d-wizard comes with the team plugin, so most people have nothing to install. For your own copy, upload a `d-wizard.skill` file, which is the [d-wizard](d-wizard) folder zipped. In Claude, go to Customize > Skills, click **+**, then **Create skill**, then **Upload a skill**, and choose the file. If an older d-wizard is already in your list, delete it first.
- **Claude Code:** copy the [d-wizard](d-wizard) folder into `~/.claude/skills/` (on Windows, `C:\Users\<you>\.claude\skills\`). If you sign in to Claude Code with your Claude account, a skill installed in Claude shows up there too.

## How it works

1. **Ask for a round.** Say "d-wizard this" and name the topic. Claude may also start one on its own when decisions need weighing.
2. **Get the round file.** In Claude it arrives as a file in the chat. In Claude Code it lands in `wizard-rounds/` in your project.
3. **Load and answer.** Open the wizard, press **Load**, and choose the file, drag it in, or paste it. Answer each question, or skip it to leave it open.
4. **Send the answers back.** Choose **Copy answers JSON** in the companion's menu or on the last screen, and paste it to Claude. Or use **Save round JSON file** and give Claude the file. In Chrome or Edge, saving writes the answers into the round file itself, so in Claude Code you just say the answers are ready.

## Your answers stay with you

Rounds and answers are kept in your own browser, and files go only where you save them. Nothing you answer is sent anywhere; the page only loads its fonts from Google Fonts.

## What's in this repository

- `index.html`: the wizard, and this site's homepage.
- `d-wizard/`: the skill. This folder is its source; `references/example-round.json` is a complete worked round.
- `.nojekyll`: tells GitHub Pages to serve every file exactly as uploaded.

## Versions

- **Wizard: 0.2.0.** It's shown at the bottom of the wizard's Options panel.
- **Skill: 0.2.0.** It's in the skill's `SKILL.md`.

A minor update bumps the last number (0.2.1). A major update bumps the middle number (0.3.0).

### Changes

- **Wizard 0.2.0:** A question can carry a `question` line: the title shows small as the topic, and the question shows large under it, while the sidebar and the summary keep the title. The options now come first, and the context sits in a panel under them: the framing, quote cards (two sources side by side), notes, links, and buttons for popups. A question can have several popups, and they are redesigned, with colored tables and quote, note, and code blocks. Number keys no longer answer behind an open popup, and a click outside closes it. The answers export carries the question after the title. Lines that open with an Arabic term in brackets, like "[القهوة]: most Qahwa wins", now read in the right direction.
- **Skill 0.2.0:** Titles name the topic and are never questions, and every question has a plain question line. Context stays in full: the skill judges what each question needs, keeps quotes that are important to understanding it, and splits longer material into labeled popups. Decisions stay decided: a pick, a typed answer, or a position stated in a comment is never asked again. Needs wizard 0.2.0.
- **Skill 0.1.1:** In Claude Code, opens the hosted wizard after the first round of a session.
- **Skill 0.1.0:** Points anyone without a wizard to the hosted page.
- **Wizard 0.1.0:** First stamped version. It has a library of rounds kept in the browser, Load and Save for round files, the Quill and Swoop companions, option cards, follow-up questions, a round timer, and light and dark themes.
