# Decision Wizard

Answer Claude's decision rounds one question at a time, then hand the answers back.

The Decision Wizard is a single web page that works with Claude's **d-wizard** skill. Claude writes your open decisions into a round file. You load it here and answer it. Claude then acts on each answer and reports where it landed.

**Open the wizard: https://AbdurrahmanKh.github.io/decision-wizard/**

## Install it as an app

The hosted wizard installs as an app, with its own window and icon. It opens offline, and whenever you're online it loads the newest version.

- **On a computer,** in Chrome or Edge: open the wizard's Options and press **Install**, or use **Install app** in the browser's menu.
- **On Android,** in Chrome: open the page, then **Install app** from the menu, or the **Install** button in Options. It replaces a shortcut to the page.
- **On an iPhone or iPad,** in Safari: **Share**, then **Add to Home Screen**.

A local copy of `index.html` keeps working as a plain page; installing is for the hosted wizard.

## Install the skill

- **Claude:** d-wizard comes with the team plugin, so most people have nothing to install. For your own copy, download `d-wizard.skill` from the [latest release](https://github.com/AbdurrahmanKh/decision-wizard/releases/latest) and upload it. In Claude, go to Customize > Skills, click **+**, then **Create skill**, then **Upload a skill**, and choose the file. If an older d-wizard is already in your list, delete it first.
- **Claude Code:** copy the [d-wizard](d-wizard) folder into `~/.claude/skills/` (on Windows, `C:\Users\<you>\.claude\skills\`). If you sign in to Claude Code with your Claude account, a skill installed in Claude shows up there too.

## How it works

1. **Ask for a round.** Say "d-wizard this" and name the topic. Claude may also start one on its own when decisions need weighing.
2. **Get the round file.** In Claude it arrives as a file in the chat, even when Claude can reach your folders. In Claude Code it lands in `wizard-rounds/` in your project.
3. **Load and answer.** Open the wizard, press **Load**, and choose the file, drag it in, or paste it. Answer each question, or skip it to leave it open.
4. **Send the answers back.** Choose **Copy answers JSON** in the companion's menu or on the last screen, and paste it to Claude. Or use **Save round JSON file** and give Claude the file. In Chrome or Edge, saving writes the answers into the round file itself, so in Claude Code you just say the answers are ready.

## Project folders, for Claude Code

A round Claude Code writes names its project and the `wizard-rounds/` folder it's in. The first time you load a round from a project, the wizard says which project it's from and where it will save, and asks you to pick that folder once, because a web page can't open a folder from a written path. The wizard checks that the folder holds the round, then remembers it for the project. You can also start from the folder: **Open a project folder** in Load connects it and opens its newest round that has no answers yet. From then on:

- **Your answers save themselves.** Each answer is written into the round's file a moment after you give it. When you're done, tell Claude the answers are ready; there's nothing to copy.
- **New rounds open by themselves.** A round that lands in the folder opens right away. If you're partway through another round, it waits in **Load** instead, with a notice and a count on the Load button.
- **Corrected rounds arrive too.** When Claude rewrites a round you've started, the answers to questions that didn't change stay. If an answer would be cleared, the new version waits: **Review** on the round lets you keep yours or replace them.

This works in Chrome and Edge on a computer, while the wizard is open. In a browser tab, the browser asks for your OK again on a later visit: choose **Allow on every visit** there, and it stops asking. The installed app keeps access by itself. **Load** lists the folders the wizard has, each with **Forget**.

## Your answers stay with you

Rounds and answers are kept in your own browser, and files go only where you save them. With a project folder connected, your answers are also written into that folder's round files, and nowhere else. Nothing you answer is sent anywhere; the page only loads its fonts from Google Fonts.

Each copy of the wizard keeps its own list of rounds, and clearing a browser's site data erases that list. **Back up all rounds**, in the Load panel and next to Clear everything in Options, writes every round and its answers to one file. Load that file in any copy of the wizard to bring the rounds back: it adds what's missing, updates what the backup has a newer copy of, and asks before touching a round that changed after the backup was made.

## What's in this repository

- `index.html`: the wizard, and this site's homepage.
- `manifest.webmanifest`, `sw.js`, and `icons/`: what makes the hosted wizard installable as an app, with its icons. The service worker keeps a copy for offline use and loads the newest version whenever you're online.
- `d-wizard/`: the skill. This folder is its source; `references/example-round.json` is a complete worked round.
- `.nojekyll`: tells GitHub Pages to serve every file exactly as uploaded.

## Versions

- **Wizard: 0.6.1.** It's shown at the bottom of the wizard's Options panel.
- **Skill: 0.5.1.** It's in the skill's `SKILL.md`. It needs wizard 0.3.0 or later, 0.4.0 for rounds with ranking, number, or bracket questions, and 0.6.0 for project folders.

A minor update bumps the last number (0.2.2). A major update bumps the middle number (0.3.0). What changed in each version is in [CHANGELOG.md](CHANGELOG.md).
