# Making a companion

Read this only when the user asks you to make a companion for the Decision Wizard: a character who sits beside the cards, changes pose, and says short lines. Often the request is a prompt the wizard wrote, starting "Make a companion for my Decision Wizard." (see From the wizard's prompt). Companions need wizard 0.7.0 or later, in Chrome or Edge on a computer.

## What a companion is

A folder. The user keeps one companions folder on their computer, and each companion is a folder inside it:

```
Inky/
  idle.svg
  greet.svg
  ...
  companion.json
```

- **Pictures** are named after the pose they fill: `idle.svg`, `greet.png`, and so on. SVG, PNG, WebP, or GIF. Only `idle` is required.
- **`companion.json`** gives the name and the lines. It's optional: without it, the folder's name is the companion's name and it never talks.
- **The whole folder** must stay under 5 MB.

## From the wizard's prompt

The wizard's Create with Claude panel, in its companion builder, writes a prompt from what the user describes. It carries only the description: everything about the folder, the frame, the poses, and the lines is in this file.

- **Name:** use it. "pick one that suits it" means the choice is yours: a short name that fits the look and the mood, never Quill, Swoop, or None.
- **About:** the few words shown after its name ("the little dragon"), kept as `about`. When it's left to you, write a few.
- **Title:** a role or nickname, like "keeper of the hoard". Use it in some of its lines; it isn't the name and isn't shown.
- **Look, art style, and pose details:** draw from them. A pose without details is drawn in the same style, as its moment suggests.
- **Sound:** a sound it makes. Work it into some of its lines, not all.
- **Mood:** up to three words. They set the voice of its lines and the faces and gestures of its poses.
- **Its lines in:** write every line in that language.
- **Reference images**, when the user attaches some: take shapes, colors, and features from them, and draw in the frame and the style the prompt asks for.
- **A character of their own:** draw only original characters. If the look describes a known character from a show, game, film, or brand, say so in one line and offer an original character instead.
- **brief:** write the description into `companion.json` (see below), so it can be described again later.

## The 14 poses

| Pose | What it shows | When it's missing, it uses |
|---|---|---|
| idle | standing, at rest | (required) |
| blink | idle with eyes shut, shown for a moment now and then | no blink |
| greet | a wave or hello | idle |
| pick | pleased, an answer was given | greet |
| skip | a shrug, a question was skipped | idle |
| milestone | proud, halfway or a batch done | pick |
| warn | worried, something is about to be cleared | idle |
| error | puzzled, a file didn't load | warn |
| finish | celebrating, the round is done | milestone |
| yawn | sleepy | idle |
| sleep | asleep | idle, with a Zzz drawn over it |
| wake | wide awake again | greet |
| dance1 | first dance step | finish |
| dance2 | second dance step | dance1 |

The dance steps through dance1, dance2, and finish while the whole figure sways. Make every pose, unless the user asks for fewer: borrowed poses work, but a companion with all 14 feels alive.

## Drawing

- **One frame for every pose:** 200 wide by 262 tall. For SVG, use `viewBox="0 -12 200 262"`, with the feet near the bottom and a soft shadow under them. Keep the character in the same place from pose to pose, so it doesn't jump.
- **The frame is small:** about 145 by 190 pixels on a wide screen and 49 by 64 on a narrow one. Use bold shapes and a clear silhouette, and avoid fine detail and text.
- **Both themes:** the wizard has a dark and a light theme, so give the character its own outline (the built-in companions use flat colors with a `#1B1810` outline) and no background.
- **Pixel art:** draw it small (under 100 pixels wide, in about the same 200 by 262 shape) as PNG, WebP, or GIF. The wizard keeps its edges crisp when it scales up.
- **SVG** must be plain drawing: no scripts, no links to other files, no embedded fonts. The wizard shows it as an image.

## companion.json

```json
{
  "name": "Inky",
  "about": "the octopus",
  "lines": {
    "greet": ["{Decisions}. Good thing I brought eight arms."],
    "pick": ["Inked.", "Noted in my best handwriting."],
    "opt_hello": "Inky here. Pens ready."
  }
}
```

- **`name`:** up to 30 characters, never Quill, Swoop, or None. The name is the companion's identity: adding another companion with the same name replaces it, after asking.
- **`about`:** a few words shown after the name, as in "Inky, the octopus". Optional.
- **`brief`:** the description the companion was made from, when it came from the wizard's prompt: `{"title": "...", "look": "...", "style": "...", "poses": {"sleep": "..."}, "sound": "...", "mood": ["..."], "language": "..."}`, leaving out what wasn't given. Optional; the wizard keeps it but doesn't show it.
- **`lines`:** each moment below names a list of lines, or one line. Write as many as the Lines column recommends: five where the moment comes up again and again, so it stays fresh; three for suggest; two for warn; and one for the moments that say the same thing each time (speed, the recaps, open_go, and the Options moments). Fewer is fine when the user asks; a moment with no lines stays quiet. A moment name the wizard doesn't know, a line that isn't text, or a placeholder the moment can't fill keeps the whole companion out, with a notice saying why.

## Lines

Lines are short (a sentence, two at most), light-hearted, in the companion's own voice, and in any language. They show in a speech bubble for a few seconds.

- Don't mention Claude.
- A `suggest` line must work whoever `{other}` names, since the user may have many companions, and on any round it comes up on, so it never says which round it is ("Round two?").
- Use only the placeholders each moment lists. `{Decisions}` and `{Picked}` start a sentence ("Seven decisions"); `{cname}` is ", Name" or nothing, so it goes right before punctuation ("Morning{cname}!").

| Moment | When it plays | Placeholders | Lines |
|---|---|---|---|
| greet | a round opens | `{Decisions}` | 5 |
| estimate | after greet, how long the round may take | `{minutes}` | 5 |
| morning | first round of a morning | `{cname}` | 5 |
| late | a round opened late at night | `{cname}` | 5 |
| back | the user, who gave a name, opens a round | `{cname}` | 5 |
| suggest | the day's second round, and every ninth, offering another companion | `{other}` | 3 |
| pick | an answer after some thought | | 5 |
| skip | a question skipped | | 5 |
| speed | an answer given the moment the question appeared | | 1 |
| second | the same answer changed a third time | | 5 |
| nudge | a question sitting a while with no answer | | 5 |
| batch | a card of rows to answer one by one | `{Decisions}` | 5 |
| half | half the round answered | | 5 |
| last | the last question | | 5 |
| finish | every question answered | | 5 |
| recap_done | the summary, nothing open | `{Picked}`, `{typedPart}`, `{timePart}` | 1 |
| recap_open | the summary, some still open | `{Picked}`, `{typedPart}`, `{ids}` | 1 |
| recap_none | the summary, nothing answered | `{ids}` | 1 |
| remind | finished, answers not copied yet | | 5 |
| copied | answers copied | | 5 |
| open_go | jumping to a question still open | `{id}` | 1 |
| stat_r | a remark on rounds finished | `{r}` | 5 |
| stat_t | a remark on answers the user wrote | `{t}` | 5 |
| stat_today | a remark on decisions today | `{td}` | 5 |
| wake | woken from a nap | | 5 |
| poke | five quick taps on the companion | | 5 |
| word | the user typed "wizard" | | 5 |
| warn | before answers are cleared | `{answers}` | 2 |
| error | a file didn't load | | 5 |
| opt_hello | chosen in Options | | 1 |
| opt_name | the user typed their name in Options | `{name}` | 1 |
| opt_light, opt_dark, opt_system | the theme changed | | 1 |
| opt_large, opt_compact, opt_normal | the text size changed | | 1 |
| opt_soundon, opt_soundoff | sounds turned on or off | | 1 |
| opt_quipson, opt_quipsoff | remarks turned on or off | | 1 |
| opt_talkon | speech bubbles turned back on | | 1 |
| opt_timereset | the round timer reset | | 1 |

## Handing it over

- **Check it first:** every SVG parses and shows the character in the frame, `companion.json` is valid JSON, its moments are all in the table above, and every placeholder is one its moment lists. The wizard refuses the whole companion over one bad line.
- **In Claude:** zip the companion's folder (the zip holds the folder itself, named after the companion) and give it to the user as a file in the conversation. They drop the zip on the wizard as it is, with wizard 0.7.3 or later; the wizard shows the companion and asks before adding it. With an older wizard, they unzip it first, then drop the folder on the wizard or use Add in the Companion card of Options.
- **In Claude Code:** if the user gives you the path of their companions folder, write the companion's folder straight into it; the wizard picks it up by itself within seconds. If a folder with that name is already there, ask before writing over it. Without the path, write the folder where the user asks. Never write a companion into a project's `wizard-rounds/` folder or into a repository.
- Say in one or two sentences what you made: its name, how many poses it has, and which moments it talks in.
- To change a line or a picture later, the user can choose Edit beside the companion in the Companion card of Options, which opens it in the wizard's builder (wizard 0.7.2 or later). Create, next to Add in the same card (Build before wizard 0.11.5), makes a new one from pictures of their own, and Create with Claude in the builder writes a prompt for a new one.
