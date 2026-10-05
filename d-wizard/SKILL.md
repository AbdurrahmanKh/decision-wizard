---
name: "d-wizard"
description: Communicate a set of questions, decisions, or approvals as a Decision Wizard questions JSON instead of long prose. Use this skill whenever the user says "d-wizard", "communicate through the wizard", "wizard this", "ask me through the wizard", "decision wizard", "decision round", or asks to turn open questions into a wizard; and proactively when open decisions need evidence attached to be answered well (conflicting sources, a table to compare), when content items need one-by-one approval (copy lines, assets, table rows, sections), or when new open decisions come up while acting on a previous round's answers, on any topic. Also use it to interpret and act on an answers JSON the user pastes back or points to as a file, recognizable by meta.tool = "decision-wizard". Do not use it for quick clarifications, for approving your own next steps, for a single question, or for questions meant for a teammate.
metadata:
  version: "0.4.0"
compatibility: Needs Decision Wizard 0.3.0 or later, and 0.4.0 for rounds with ranking, number, or bracket questions. Older wizards still open plain rounds, but show no recommendations and give no way to add a note to a pick.
---

# Decision Wizard

The Decision Wizard is a standalone HTML page, hosted at https://abdurrahmankh.github.io/decision-wizard/; the user may also keep a copy of their own. You will never see it, never generate it, and never edit it; it may not even exist in your context, and that is fine. Your entire job is to produce one valid **questions JSON**. The user loads it into their wizard, clicks through the questions one at a time, and returns an **answers JSON**, pasted or as a file. This replaces walls of prose: instead of explaining five issues in one long message, you ship five self-contained questions and receive five decisions.

If the user asks where the wizard is, or may not have one, point them to https://abdurrahmankh.github.io/decision-wizard/. Any copy of the wizard, hosted or their own, opens any valid questions JSON. Do not attempt to build or describe the HTML, and never open, read, or edit the user's own copy.

## When to use it, when not

An explicit request always fires it. Without one, use it when:

- the questions need evidence attached to be answered well: two sources that conflict, a table to compare, a quote to judge;
- content items need one-by-one approval: copy lines, assets, rows of a table, sections of a document;
- you are acting on a previous round's answers and new open decisions come up: they go into the next round, not into prose.

Do not use it for quick clarifications that need no evidence (which folder, which test runner, okay to install a package), for approving your own next steps (a refactor plan, the order of edits), or for one blocking yes or no question. For those, use the environment's native multiple-choice prompt when one exists, otherwise just ask. Decisions meant for a teammate go as a plain question in the message. Never use it to deliver information that requires no decision.

## The two rules that outrank the rest

### Every question carries the context it needs, and the wizard keeps it from overwhelming

Context is the heart of the wizard: a reader with zero chat history, opening a question days later, has everything needed to answer it well. Never cut context to make a card shorter. For each question, judge what helps someone answer it, and include all of that, long when the question needs it. What changes is where each piece goes:

- **The title and the question come first.** The title names the topic. The question asks the decision in plain words and reads on its own: "How should trophies pay their achievement points?". Together they orient the reader before any context.
- **`context` is the framing:** why this question exists, what is at stake, what changed. As many sentences as the question needs.
- **`detail` is the evidence the answer depends on.** A quote earns its place by being important to understanding the question, such as the two sources that conflict or the exact rule being changed, never because it relates to the topic. Notes say what each answer implies. Code shows the exact thing being decided.
- **`extra` holds what helps but isn't needed to answer,** behind buttons: full tables, background, longer comparisons. Split it by topic into several popups, each labeled with what is inside ("Show the provider comparison"), rather than one long popup.

The wizard shows the question and its options first, with the context in a panel under them, so a reader who remembers answers at once and a reader who doesn't reads on.

Self-contained also means a question never leans on memory: never write "as discussed", "see my earlier message", or "(round 1, C4)". When a question builds on earlier decisions, state each one in plain words where it is needed: "you decided every request notifies all members".

### Decisions stay decided

A decision is made the moment the user gives it: a picked answer, a typed answer, or a position stated in a comment, including a comment next to Discuss or Rework and a note on a question left open. From then on it is settled, and asking it again wastes the user's time.

- Never put a settled decision into a later round: not as a question, not as a row to confirm, and not as a note that hands the user's own words back to them.
- When you agree with what the user wrote, that is the decision. Say so in your reply in one line; don't ask them to confirm it.
- When a comment asks something and also states a lean ("how would images fit in a JSON? I don't think we need it"), answer the question in your reply and take the lean as the decision. Bring it back only if your answer would likely change their mind, and say why in one line.
- Reopen a decision only when the user asks, or when a new fact would change it. Then ask only what changed, and say in one line what it was.
- Before delivering a round, check each question against what is already decided in the conversation and in the files you were given, and drop anything settled.
- Options name what happens, never agreement with a note: "Approve" next to a note saying a feature isn't needed reads both ways.

## The questions JSON

Top level:

```json
{
  "config": { "title": "Round title", "tagline": "One line under the title", "product": "Team or product label", "needs_wizard": "0.3.0" },
  "questions": [ ]
}
```

`config.needs_wizard` names the oldest wizard the round is made for: `"0.4.0"` when the round has a ranking, number, or bracket question, and `"0.3.0"` otherwise. A wizard older than the version a round names warns when the round loads.

`config.title` is the round's identity in the user's wizard. The wizard keeps every round the user loads, and a round arriving with the title of one already saved replaces it as a new version: answers carry over for questions whose id, title, question, and options are unchanged (in a batch, rows whose id and label are unchanged), and the wizard asks before clearing the rest. So give every new round its own title that names the round number ("Checkout Redesign, Round 2"). Reuse a title only to resend a corrected version of the same round, and keep every unchanged question identical so its answer survives.

Per question:

| Field | Required | What it does |
|---|---|---|
| id | yes | One letter plus a number ("A1", "B3"), two letters only when one letter is ambiguous ("CR1" next to "CO1"). The letter usually encodes the section. Ids render on the question card and key the answers, so keep them short and stable across revision rounds. Every id is unique in the round, and every row id is unique within its batch; the wizard refuses to load a round that repeats one |
| section | yes | Groups questions in the sidebar. Order sections by importance, blocking decisions first |
| title | yes | The topic, as a short label: "Season trophy location", "How a trophy pays achievement points". It shows small above the question, and alone in the sidebar and the summary. Never a question, direct or indirect: no question mark, and no opening "Where", "Which", "Whether", "Should", or "How many" |
| question | yes | The decision as one plain question, readable alone, ending with a question mark: "Where should the season trophy sit?". It shows large on the card and comes back with the answer. Write one for every question and follow-up |
| context | no | The framing: why this question exists, what is at stake, what changed. As long as the question needs. Shown at the top of the Context panel, under the options |
| detail | no | Evidence the answer depends on, shown in the Context panel under the options. Quote what is important to understanding the question, not everything related to the topic. `{"kind":"quote","src":"Source name","text":"Verbatim quote"}` renders as a highlighted block with a source label. `{"kind":"note","text":"..."}` renders as a muted note; use notes for what each answer implies. `{"kind":"code","src":"path/to/file.js","text":"..."}` renders as monospace code that keeps its indentation and scrolls sideways, with `src` shown exactly as written, so file paths keep their case; use it for code, config, or exact strings. Code blocks work in `detail` and in popups |
| links | no | Array of `{"label":"...","url":"https://..."}`. Open in a new tab. Real URLs only, never fabricated |
| extra | no | Popups behind buttons, for what helps but isn't needed to answer: `{"label":"Button text","blocks":[...]}`, or a list of them for several buttons, one per topic. Blocks are `{"kind":"text","text":"..."}`, `{"kind":"table","title":"...","columns":[...],"rows":[[...]]}`, or the quote, note, and code blocks of `detail`. Every row must have exactly as many cells as columns |
| options | yes | Array of answer strings, or of cards. A card is `{"label":"Short title","text":"What picking this route means"}`: the label is the answer that comes back, the text is the one or two sentences that make the route clear. Use cards for two or three routes that each need explaining; the wizard refuses more than three cards on a plain question, and cards in a batch. Labels are unique within a question. Clicking one records it and advances. A number question takes `min` and `max` instead (see below) |
| customLabel | no | Label for the typed-answer option, naming what to type (e.g. "New thresholds (type them)"). Defaults to "Custom answer (type it)" |
| custom | no | `false` removes the typed-answer option |
| skip | no | `false` removes the Skip button. Use rarely; skipping exports the question as still open, which is usually the honest state |
| recommend | no | The label of the option you recommend, spelled exactly as in `options`. The wizard marks it with a small wizard hat. Works on single questions, cards, and follow-ups; on a grouped question, put it on each row instead. The wizard refuses a round whose `recommend` names no option |
| because | no | Your reason, one line written to finish the sentence "I recommend this because": `"because": "it keeps the 41% of purchases that come through guest checkout."`. The wizard shows it under the recommended option, and on a grouped row as "I recommend Rework because ...". Only with `recommend` |
| followups | no | Questions that open under the same issue once its answer calls for them, on single questions only: `"followups":[{"id":"F1a","when":["It rises"],"title":"How it climbs","question":"How fast should it climb?","options":[...]}]`. `when` lists the main question's option labels that open the follow-up, spelled exactly; leave it out to open on any answer, a typed one included. A follow-up takes `question`, `context`, `detail`, `links`, `options` (strings or cards), `customLabel`, `custom`, `recommend`, and `because`, but not `extra`, `type`, or follow-ups of its own. Its id is unique across the round. It counts under its issue, so the wizard moves on only once every follow-up that opened is answered |
| type + items | no | `"type":"batch"` turns the question into a table: `"items":[{"id":"row1","label":"Row label","note":"Optional context under the label"}]`. Every row takes one answer from the shared options set, and a row can carry its own `recommend` and `because`, naming one of the shared options |

Every question, follow-up, and grouped row also has a pen for the user's note, so a pick can come back with a condition attached ("B, but only for clans over 20 members"), and a question can come back open with only a note. You don't add anything to the round for it.

### Ranking, number, and bracket questions

Three more values of `type` change how a question is answered. Each takes the usual `id`, `section`, `title`, `question`, `context`, `detail`, `links`, `extra`, `customLabel`, and `custom`, but not follow-ups. Any round that uses one sets `needs_wizard` to `"0.4.0"`.

| Type | What the round gives | What the user does | What comes back |
|---|---|---|---|
| `"rank"` | `options`, 2 to 10, strings or cards. `recommend` is the whole order you recommend, as a list of every option label, best first | Drags the rows into order, or moves them with arrows, then records the order | `"status":"ranked"`, and `answer` is the list of labels, best first |
| `"number"` | `min`, `max`, `step` (1 when left out), and `unit` (optional, such as `"ms"` or `"%"`), and no `options`. `recommend` is a number in the range | Sets a slider or types the exact value, which snaps to the range and the step, then records it | `"status":"picked"`, `answer` as a number, and `unit` when the question has one |
| `"bracket"` | `options`, 4 to 32, strings or cards. `recommend` is one option label | Picks the better of each pair, knockout style, until one is left | `"status":"picked"`, `answer` as the winner, and `matches`: every match as `{"round":1,"pair":["A","B"],"winner":"A"}` |

When recommendations are on, a ranking starts in your recommended order and a number starts on your recommended value, with the hat and "I recommend this order because..." or "I recommend 4,500 ms because..." above them. With no recommendation, a ranking starts in the listed order and a number in the middle of its range. On a bracket, the hat marks your option in every match it plays.

A bracket pairs options in the listed order: 1 meets 2, 3 meets 4, and the winners keep pairing until one is left. With 8 options, options 1 to 4 and 5 to 8 meet only in the final, so list the strongest options far apart. When the count isn't 4, 8, 16, or 32, the first options in the list skip round 1, and in round 2 each of them meets a round-1 winner: with 6 options, 1 and 2 skip round 1 while 3 meets 4 and 5 meets 6, so list the strongest first.

## Authoring rules

- One decision per question. A compound question splits into two.
- Quotes are verbatim from real sources, with `src` naming the source, and each one is important to understanding the question. Never invent a quote. When two sources conflict, quote both side by side; the conflict is the question.
- When the true rationale or fact is not on record, options are candidates only: say so in a note ("picking one asserts it as the real reason") and include an honest escape such as "Leave unrecorded" or "Unknown: route to engineering".
- Include a keep-open or route-to-owner option whenever forcing a decision would be wrong. The wizard is for collecting decisions, not extracting them.
- Options are short and mutually exclusive. Consequences go in a note, or in a card's text, never inside option labels.
- When the decision is a choice between two or three routes that each need a sentence to understand, make the options cards: the label names the route, the text says what it means. Every alternative is its own option. Never put one alternative in a row's label and the other in its note, or one in the question and the other in the context. When several items each need their own alternatives, write one card question per item rather than a batch.
- When a question only matters after a certain answer ("only needed if", "skip it otherwise"), make it a follow-up of that question with `when`. Never ship it as a standalone question that tells the user when to skip it.
- Try to batch, actively. AI-authored rounds under-batch by default, so before delivering, scan the round: three or more questions sharing one answer set (Approve / Rework, Keep / Remove, Yes / No) are one batch question you failed to make. Fold them. Per-row context goes in the item's `note`; the full source material goes in `extra`. The only reason not to batch is items genuinely needing different answer sets.
- Pick the question type from the shape of the answer. An order (priorities, a sequence of work) is a ranking. A number (a threshold, timeout, limit, count, or percentage) is a number question, never a list of numbers as options. One winner from four or more options that compare best head to head is a bracket. Two or three routes that each need a sentence are cards.
- Recommend wherever you have a view. Put `recommend` on every question where you would pick one option, order, or value, and add `because` whenever you have a reason, which should be most of the time. Base it on the evidence in the question, and keep the context complete: the hat is a pointer, never a substitute for what the reader needs to judge the question. Leave it off when you have no basis for a view, and never recommend against a decision the user already made.
- Long tables and long text go in `extra`, split into labeled popups by topic, never crammed into the card.
- Write in the user's working language. Right-to-left text is safe in every field.
- No em dashes and no en dashes anywhere in the content; use hyphens, colons, or periods.

For a complete worked round demonstrating every feature, read `references/example-round.json`.

## Delivering a round

File first. Whenever you can write files, deliver the round as a `.json` file named `<YYYY-MM-DD>-<topic>-round<N>.json` (today's date, a short kebab-case topic, the round number) and give its path in the message.

- Working inside a project folder (a git repository): write the file to `wizard-rounds/` at the project root. The first time you write a round in a project, check that `wizard-rounds/` is listed in the project's `.gitignore` and add it if it is not.
- Anywhere else: write it wherever your file outputs go, and make it visible to the user the way your environment shows files.
- Only when no file tools exist: output the JSON in a single fenced `json` code block.

Surround the round with at most two sentences. Do not restate the questions in prose; the JSON is the communication, and duplicating it defeats the purpose. Tell the user to load the file into their wizard, at https://abdurrahmankh.github.io/decision-wizard/ if they don't have one, or to paste the block, and to return the exported answers as a paste or a file path.

In Claude Code, after writing the first round of a session, also open the hosted wizard in the user's browser so it is ready to load the file: run the system's command for opening a link (`open` on macOS, `xdg-open` on Linux, `start` or `Start-Process` on Windows) with https://abdurrahmankh.github.io/decision-wizard/. Claude Code asks the user's permission before running it unless they have already allowed it. Open it once per session, not for every round; skip it if the user has said not to; and never open a local copy. Where you cannot run commands, as in Claude, give the link instead.

## Consuming the answers JSON

The answers arrive pasted in the chat or as a file path. Recognize them by `meta.tool = "decision-wizard"`, never by file name. If the user says the answers are ready without giving a path or a paste, look in `wizard-rounds/` for the newest `.json` file whose `meta.tool` is `decision-wizard`. A round file you wrote carries `config` at the top level and no `meta`, but it can come back changed: when the user opens a round file in a browser that allows it and saves, the wizard writes the answers into that same file. Downloaded saves are named `<title>-answers-<YYYY-MM-DD>.json`. If nothing is there, ask for the path or a paste.

What comes back:

```json
{
  "meta": { "tool": "decision-wizard", "wizard_title": "...", "exported_at": "...", "total": 9, "answered": 8, "open": 1 },
  "answers": [
    { "id": "A1", "section": "...", "issue": "The title", "question": "The question", "status": "picked", "answer": "The chosen option text", "comment": "The user's note, when there is one" },
    { "id": "A2", "section": "...", "issue": "...", "status": "custom", "answer": "What the user typed" },
    { "id": "A3", "section": "...", "issue": "...", "status": "open", "answer": "" },
    { "id": "A5", "section": "...", "issue": "...", "status": "open", "answer": "", "comment": "A note with no pick" },
    { "id": "R1", "section": "...", "issue": "...", "status": "ranked", "answer": ["Best", "Next", "Last"] },
    { "id": "N1", "section": "...", "issue": "...", "status": "picked", "answer": 4500, "unit": "ms" },
    { "id": "K1", "section": "...", "issue": "...", "status": "picked", "answer": "Winner", "matches": [ { "round": 1, "pair": ["Winner", "Other"], "winner": "Winner" } ] },
    { "id": "A4", "section": "...", "issue": "...", "status": "picked", "answer": "It rises",
      "followups": [ { "id": "A4a", "issue": "...", "status": "picked", "answer": "Double each level" },
                     { "id": "A4b", "issue": "...", "status": "not_needed", "answer": "" } ] },
    { "id": "B1", "section": "...", "issue": "...", "status": "batch", "answered_items": 4, "total_items": 5,
      "items": [ { "id": "row1", "label": "...", "answer": "Approve", "comment": "" } ] }
  ]
}
```

`issue` is the title and `question` is the question; rounds made before the question line come back without `question`. A ranking comes back with `"status":"ranked"` and its list, best first; a number question with a number and its `unit`; a bracket with its winner and every match. A note the user wrote comes back as `comment` on its question, follow-up, or row; questions and follow-ups without one have no `comment` field. A file saved from the wizard carries the same `meta` and `answers`, plus the whole round under `round` (`{"config": {...}, "questions": [...]}`). When `round` is present, it is the exact version the user answered: read options, notes, and row labels from it, and use it to reconcile ids.

Handling rules:

- `open` means still undecided. Record it as open wherever the decision lives. Never fill it in yourself.
- Every answer, typed answer, and position stated in a comment is settled, per Decisions stay decided. A Discuss or Rework answer whose comment states a position is that position; only what the comment leaves open is still open.
- `custom` is the user's verbatim decision and is authoritative. Act on it. Ask a follow-up only when it is genuinely ambiguous, and quote the ambiguous part when asking.
- A `comment` next to a pick is part of the decision: act on the pick with the comment's condition or detail attached. A `comment` on an open question works like Discuss: a position it states is settled, and only what it leaves open stays open.
- Follow-ups come back inside their issue. `not_needed` means the main answer did not call for it: record it as not applicable and never answer it. A follow-up still `open` under an answered main question means the issue is only partly decided, and `meta.answered` does not count it.
- A bracket's `matches` show more than the winner: the loser of the final is the runner-up, often the fallback. A bracket still `open` may carry the matches played so far; it's undecided until it has a winner.
- In batches, a comment belongs to its row. A rework-style answer plus a comment means: apply the comment and show the reworked result for a quick re-approve. A comment without an answer is context, and the row is still open.
- Unmatched ids on import mean the round changed between export and import; reconcile before acting on anything.
- After acting on a round, report back per id where each decision landed (which document, which system, or still open). The user should be able to trace every answer to its consequence.
