#!/usr/bin/env python3
"""Prints a Decision Wizard round's answers, one compact line per id.

Usage: python3 read_answers.py FILE [--full]

FILE is a round file the wizard saved answers into, a saved answers file, or
an answers JSON. When FILE is a round with no answers yet, the newest answers
file with the same title in the same folder is read instead.
--full adds each question and the text of a picked card.
Exits 0 with answers printed, or 2 when no answers have arrived.
"""

import glob
import json
import os
import sys


def load(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def has_answers(data):
    return isinstance(data, dict) and (data.get("meta") or {}).get("tool") == "decision-wizard"


def find_answers(path, title):
    folder = os.path.dirname(os.path.abspath(path))
    matches = []
    for candidate in glob.glob(os.path.join(folder, "*.json")):
        try:
            data = load(candidate)
        except (OSError, ValueError):
            continue
        if has_answers(data) and data["meta"].get("wizard_title") == title:
            matches.append((os.path.getmtime(candidate), candidate, data))
    return max(matches)[1:] if matches else (None, None)


def index_round(round_data):
    """Maps each question, follow-up, and row id to its source in the round."""
    found = {}
    for item in (round_data or {}).get("questions", []):
        found[item.get("id")] = item
        for followup in item.get("followups") or []:
            found[followup.get("id")] = followup
    return found


def card_text(source, answer):
    for option in (source or {}).get("options") or []:
        if isinstance(option, dict) and option.get("label") == answer:
            return option.get("text")
    return None


def show(value):
    if isinstance(value, list):
        return " > ".join(map(str, value))
    return str(value) if value not in (None, "") else "-"


def line(entry, sources, full, indent=""):
    out = []
    answer = show(entry.get("answer"))
    if entry.get("status") == "batch":
        answer = f"{entry.get('answered_items')} of {entry.get('total_items')} rows answered"
    elif entry.get("unit") and entry.get("answer") not in (None, ""):
        answer += f" {entry['unit']}"
    name = entry.get("issue") or entry.get("label") or ""
    out.append(f"{indent}{entry.get('id')} [{entry.get('status', 'row')}] {name}: {answer}")
    source = sources.get(entry.get("id"))
    if full:
        question = entry.get("question") or (source or {}).get("question")
        if question:
            out.append(f"{indent}  question: {question}")
        text = card_text(source, entry.get("answer"))
        if text:
            out.append(f"{indent}  card: {text}")
    if entry.get("comment"):
        out.append(f"{indent}  note: {entry['comment']}")
    if entry.get("matches"):
        runner_up = next((m for m in reversed(entry["matches"]) if m.get("winner") == entry.get("answer")), None)
        if runner_up:
            loser = [p for p in runner_up.get("pair", []) if p != entry.get("answer")]
            out.append(f"{indent}  runner-up: {show(loser)}")
    for followup in entry.get("followups") or []:
        out.extend(line(followup, sources, full, indent + "  "))
    for row in entry.get("items") or []:
        out.extend(line(row, sources, full, indent + "  "))
    return out


def main():
    args = [arg for arg in sys.argv[1:] if arg != "--full"]
    full = "--full" in sys.argv[1:]
    if len(args) != 1:
        print(__doc__.strip())
        return 2
    path = args[0]
    data = load(path)
    if not has_answers(data):
        title = (data.get("config") or {}).get("title")
        other, data = find_answers(path, title)
        if not other:
            print(f"no answers yet for {title!r}: {path} is as written and no saved answers share its title")
            return 2
        print(f"answers from {other}")

    meta = data["meta"]
    print(f"{meta.get('wizard_title')}: {meta.get('answered')} of {meta.get('total')} answered, {meta.get('open')} open")
    sources = index_round(data.get("round"))
    for entry in data.get("answers", []):
        print("\n".join(line(entry, sources, full)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
