# Decision Wizard

Answer Claude's decision rounds one question at a time, then hand the answers back.

The Decision Wizard is a single web page that works with Claude's **d-wizard** skill. Claude writes your open decisions into a round file. You load it here and answer it. Claude then acts on each answer and reports where it landed.

**Open the wizard: https://AbdurrahmanKh.github.io/decision-wizard/**

## Install the skill

- **Claude:** d-wizard comes with the team plugin, so most people have nothing to install. For your own copy, download `d-wizard.skill` from the [latest release](https://github.com/AbdurrahmanKh/decision-wizard/releases/latest) and upload it. In Claude, go to Customize > Skills, click **+**, then **Create skill**, then **Upload a skill**, and choose the file. If an older d-wizard is already in your list, delete it first.
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

- **Wizard: 0.3.0.** It's shown at the bottom of the wizard's Options panel.
- **Skill: 0.3.0.** It's in the skill's `SKILL.md`. It needs wizard 0.3.0 or later.

A minor update bumps the last number (0.2.2). A major update bumps the middle number (0.3.0). What changed in each version is in [CHANGELOG.md](CHANGELOG.md).
