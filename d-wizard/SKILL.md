---
name: d-wizard
description: Communicate a set of questions, decisions, or approvals as a Decision Wizard questions JSON instead of long prose. Use this skill whenever the user says "d-wizard", "communicate through the wizard", "wizard this", "ask me through the wizard", "decision wizard", "decision round", or asks to turn open questions into a wizard; and proactively when open decisions need evidence attached to be answered well (conflicting sources, a table to compare), when content items need one-by-one approval (copy lines, assets, table rows, sections), or when new open decisions come up while acting on a previous round's answers, on any topic. Also use it to interpret and act on an answers JSON the user pastes back or points to as a file, recognizable by meta.tool = "decision-wizard". Do not use it for quick clarifications, for approving your own next steps, for a single question, or for questions meant for a teammate.
---

# Decision Wizard

The user owns a standalone HTML file called the Decision Wizard. You will never see it, never generate it, and never edit it; it may not even exist in your context, and that is fine. Your entire job is to produce one valid **questions JSON**. The user loads it into their wizard, clicks through the questions one at a time, and returns an **answers JSON**, pasted or as a file. This replaces walls of prose: instead of explaining five issues in one long message, you ship five self-contained questions and receive five decisions.

If the user asks where the wizard is: it is their own HTML file, any copy of it opens any valid questions JSON. Do not attempt to build or describe the HTML, and do not open it for the user.

## When to use it, when not

An explicit request always fires it. Without one, use it when:

- the questions need evidence attached to be answered well: two sources that conflict, a table to compare, a quote to judge;
- content items need one-by-one approval: copy lines, assets, rows of a table, sections of a document;
- you are acting on a previous round's answers and new open decisions come up: they go into the next round, not into prose.

Do not use it for quick clarifications that need no evidence (which folder, which test runner, okay to install a package), for approving your own next steps (a refactor plan, the order of edits), or for one blocking yes or no question. For those, use the environment's native multiple-choice prompt when one exists, otherwise just ask. Decisions meant for a teammate go as a plain question in the message. Never use it to deliver information that requires no decision.

## The one rule that outranks the rest

**Every question should cover the context in the best way possible, so the designer can work through each question independently.**

Independently means: a reader with zero chat history, opening this question cold, has everything needed to answer it. The evidence is quoted inside the question, not referenced. Never write "as discussed" or "see my earlier message". If answering requires reading a table, the table is in the question's popup. If it requires a source, the source is quoted or linked. Assume the answers arrive days later, possibly from a person who never saw the conversation.

This applies to your own earlier rounds too. Never reference a previous round, question id, or past answer without restating its full content in place: "(round 1, C4)" is a violation, "you decided every request pushes a notification to all members" is the rule. When a row applies decisions already made, its note states each decision in plain words.

## The questions JSON

Top level:

```json
{
  "config": { "title": "Round title", "tagline": "One line under the title", "product": "Team or product label" },
  "questions": [ ]
}
```

`config.title` is the round's identity in the user's wizard. The wizard keeps every round the user loads, and a round arriving with the title of one already saved replaces it as a new version: answers carry over for questions whose id, title, and options are unchanged (in a batch, rows whose id and label are unchanged), and the wizard asks before clearing the rest. So give every new round its own title that names the round number ("Checkout Redesign, Round 2"). Reuse a title only to resend a corrected version of the same round, and keep every unchanged question identical so its answer survives.

Per question:

| Field | Required | What it does |
|---|---|---|
| id | yes | One letter plus a number ("A1", "B3"), two letters only when one letter is ambiguous ("CR1" next to "CO1"). The letter usually encodes the section. Ids render on the question card and key the answers, so keep them short and stable across revision rounds. Every id is unique in the round, and every row id is unique within its batch; the wizard refuses to load a round that repeats one |
| section | yes | Groups questions in the sidebar. Order sections by importance, blocking decisions first |
| title | yes | The decision itself, one line |
| context | no | One or two sentences framing why this question exists |
| detail | no | Array of evidence blocks. `{"kind":"quote","src":"Source name","text":"Verbatim quote"}` renders as a highlighted block with a source label. `{"kind":"note","text":"..."}` renders as a muted note; use notes for what each answer implies. `{"kind":"code","src":"path/to/file.js","text":"..."}` renders as monospace code that keeps its indentation and scrolls sideways, with `src` shown exactly as written, so file paths keep their case; use it for code, config, or exact strings. Code blocks work in `detail` only |
| links | no | Array of `{"label":"...","url":"https://..."}`. Open in a new tab. Real URLs only, never fabricated |
| extra | no | A popup for long material: `{"label":"Button text","blocks":[...]}`. Blocks are `{"kind":"text","text":"..."}` or `{"kind":"table","title":"...","columns":[...],"rows":[[...]]}`. Every row must have exactly as many cells as columns |
| options | yes | Array of answer strings, or of cards. A card is `{"label":"Short title","text":"What picking this route means"}`: the label is the answer that comes back, the text is the one or two sentences that make the route clear. Use cards for two or three routes that each need explaining; the wizard refuses more than three cards, and cards in a batch. Labels are unique within a question. Clicking one records it and advances |
| customLabel | no | Label for the typed-answer option, naming what to type (e.g. "New thresholds (type them)"). Defaults to "Custom answer (type it)" |
| custom | no | `false` removes the typed-answer option |
| skip | no | `false` removes the Skip button. Use rarely; skipping exports the question as still open, which is usually the honest state |
| followups | no | Questions that open under the same issue once its answer calls for them, on single questions only: `"followups":[{"id":"F1a","when":["It rises"],"title":"How it climbs","options":[...]}]`. `when` lists the main question's option labels that open the follow-up, spelled exactly; leave it out to open on any answer, a typed one included. A follow-up takes `context`, `detail`, `links`, `options` (strings or cards), `customLabel`, and `custom`, but not `extra`, `type`, or follow-ups of its own. Its id is unique across the round. It counts under its issue, so the wizard moves on only once every follow-up that opened is answered |
| type + items | no | `"type":"batch"` turns the question into a table: `"items":[{"id":"row1","label":"Row label","note":"Optional context under the label"}]`. Every row takes one answer from the shared options set, and every row also accepts a free comment from the user regardless of its answer |

## Authoring rules

- One decision per question. A compound question splits into two.
- Quotes are verbatim from real sources, with `src` naming the source. Never invent a quote. When two sources conflict, quote both side by side; the conflict is the question.
- When the true rationale or fact is not on record, options are candidates only: say so in a note ("picking one asserts it as the real reason") and include an honest escape such as "Leave unrecorded" or "Unknown: route to engineering".
- Include a keep-open or route-to-owner option whenever forcing a decision would be wrong. The wizard is for collecting decisions, not extracting them.
- Options are short and mutually exclusive. Consequences go in a note, or in a card's text, never inside option labels.
- When the decision is a choice between two or three routes that each need a sentence to understand, make the options cards: the label names the route, the text says what it means. Every alternative is its own option. Never put one alternative in a row's label and the other in its note, or one in the title and the other in the context. When several items each need their own alternatives, write one card question per item rather than a batch.
- When a question only matters after a certain answer ("only needed if", "skip it otherwise"), make it a follow-up of that question with `when`. Never ship it as a standalone question that tells the user when to skip it.
- Try to batch, actively. AI-authored rounds under-batch by default, so before delivering, scan the round: three or more questions sharing one answer set (Approve / Rework, Keep / Remove, Yes / No) are one batch question you failed to make. Fold them. Per-row context goes in the item's `note`; the full source material goes in `extra`. The only reason not to batch is items genuinely needing different answer sets.
- Long tables and long text go in `extra`, never crammed into the card.
- Write in the user's working language. Right-to-left text is safe in every field.
- No em dashes and no en dashes anywhere in the content; use hyphens, colons, or periods.

For a complete worked round demonstrating every feature, read `references/example-round.json`.

## Delivering a round

File first. Whenever you can write files, deliver the round as a `.json` file named `<YYYY-MM-DD>-<topic>-round<N>.json` (today's date, a short kebab-case topic, the round number) and give its path in the message.

- Working inside a project folder (a git repository): write the file to `wizard-rounds/` at the project root. The first time you write a round in a project, check that `wizard-rounds/` is listed in the project's `.gitignore` and add it if it is not.
- Anywhere else: write it wherever your file outputs go, and make it visible to the user the way your environment shows files.
- Only when no file tools exist: output the JSON in a single fenced `json` code block.

Surround the round with at most two sentences. Do not restate the questions in prose; the JSON is the communication, and duplicating it defeats the purpose. Tell the user to load the file into their wizard (or paste the block), and to return the exported answers as a paste or a file path.

## Consuming the answers JSON

The answers arrive pasted in the chat or as a file path. Recognize them by `meta.tool = "decision-wizard"`, never by file name. If the user says the answers are ready without giving a path or a paste, look in `wizard-rounds/` for the newest `.json` file whose `meta.tool` is `decision-wizard`. A round file you wrote carries `config` at the top level and no `meta`, but it can come back changed: when the user opens a round file in a browser that allows it and saves, the wizard writes the answers into that same file. Downloaded saves are named `<title>-answers-<YYYY-MM-DD>.json`. If nothing is there, ask for the path or a paste.

What comes back:

```json
{
  "meta": { "tool": "decision-wizard", "wizard_title": "...", "exported_at": "...", "total": 9, "answered": 8, "open": 1 },
  "answers": [
    { "id": "A1", "section": "...", "issue": "...", "status": "picked", "answer": "The chosen option text" },
    { "id": "A2", "section": "...", "issue": "...", "status": "custom", "answer": "What the user typed" },
    { "id": "A3", "section": "...", "issue": "...", "status": "open", "answer": "" },
    { "id": "A4", "section": "...", "issue": "...", "status": "picked", "answer": "It rises",
      "followups": [ { "id": "A4a", "issue": "...", "status": "picked", "answer": "Double each level" },
                     { "id": "A4b", "issue": "...", "status": "not_needed", "answer": "" } ] },
    { "id": "B1", "section": "...", "issue": "...", "status": "batch", "answered_items": 4, "total_items": 5,
      "items": [ { "id": "row1", "label": "...", "answer": "Approve", "comment": "" } ] }
  ]
}
```

A file saved from the wizard carries the same `meta` and `answers`, plus the whole round under `round` (`{"config": {...}, "questions": [...]}`). When `round` is present, it is the exact version the user answered: read options, notes, and row labels from it, and use it to reconcile ids.

Handling rules:

- `open` means still undecided. Record it as open wherever the decision lives. Never fill it in yourself.
- `custom` is the user's verbatim decision and is authoritative. Act on it. Ask a follow-up only when it is genuinely ambiguous, and quote the ambiguous part when asking.
- Follow-ups come back inside their issue. `not_needed` means the main answer did not call for it: record it as not applicable and never answer it. A follow-up still `open` under an answered main question means the issue is only partly decided, and `meta.answered` does not count it.
- In batches, a comment belongs to its row. A rework-style answer plus a comment means: apply the comment and show the reworked result for a quick re-approve. A comment without an answer is context, and the row is still open.
- Unmatched ids on import mean the round changed between export and import; reconcile before acting on anything.
- After acting on a round, report back per id where each decision landed (which document, which system, or still open). The user should be able to trace every answer to its consequence.
