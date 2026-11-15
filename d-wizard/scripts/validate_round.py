#!/usr/bin/env python3
"""Checks a Decision Wizard questions JSON against the rules in SKILL.md.

Usage: python3 validate_round.py ROUND.json
Prints "ok" and exits 0, or prints one problem per line and exits 1.
"""

import json
import sys

DASHES = {"–": "en dash", "—": "em dash"}
TITLE_OPENERS = ("where ", "which ", "whether ", "should ", "how many ")
TYPED = {"rank", "number", "bracket"}
MAX_CARDS = 3


def version(text):
    try:
        return tuple(int(part) for part in str(text).split("."))
    except ValueError:
        return None


def label(option):
    return option.get("label") if isinstance(option, dict) else option


class Checker:
    """Collects the problems found in one round."""

    def __init__(self):
        self.problems = []

    def fail(self, where, message):
        self.problems.append(f"{where}: {message}")

    def dashes(self, value, where):
        if isinstance(value, str):
            for char, name in DASHES.items():
                if char in value:
                    self.fail(where, f"contains an {name}; use a hyphen, colon, or period")
        elif isinstance(value, dict):
            for key, item in value.items():
                self.dashes(item, f"{where}.{key}")
        elif isinstance(value, list):
            for index, item in enumerate(value):
                self.dashes(item, f"{where}[{index}]")

    def blocks(self, blocks, where):
        for index, block in enumerate(blocks or []):
            if block.get("kind") == "table":
                width = len(block.get("columns", []))
                for row_index, row in enumerate(block.get("rows", [])):
                    if len(row) != width:
                        self.fail(f"{where}[{index}].rows[{row_index}]", f"has {len(row)} cells for {width} columns")

    def extra(self, extra, where):
        popups = extra if isinstance(extra, list) else [extra]
        for index, popup in enumerate(popups):
            self.blocks(popup.get("blocks"), f"{where}[{index}].blocks")

    def text_fields(self, item, where, needs_title=True):
        title = item.get("title", "")
        question = item.get("question", "")
        if needs_title:
            if not title:
                self.fail(where, "has no title")
            elif title.rstrip().endswith("?") or title.lower().startswith(TITLE_OPENERS):
                self.fail(where, f"title reads as a question: {title!r}")
        if not question:
            self.fail(where, "has no question")
        elif not question.rstrip().endswith("?"):
            self.fail(where, "question does not end with a question mark")

    def options(self, item, where, in_batch=False):
        options = item.get("options")
        if not options:
            self.fail(where, "has no options")
            return []
        labels = [label(option) for option in options]
        if len(set(labels)) != len(labels):
            self.fail(where, "repeats an option label")
        cards = sum(isinstance(option, dict) for option in options)
        if in_batch and cards:
            self.fail(where, "a batch takes plain string options, not cards")
        elif cards > MAX_CARDS and item.get("type") not in ("rank", "bracket"):
            self.fail(where, f"has {cards} cards; the wizard refuses more than {MAX_CARDS}")
        return labels

    def recommend(self, item, labels, where):
        if "recommend" not in item:
            if "because" in item:
                self.fail(where, "has because without recommend")
            return
        pick = item["recommend"]
        if pick not in labels:
            self.fail(where, f"recommend {pick!r} names no option")

    def question(self, item, where, ids):
        kind = item.get("type")
        for field in ("id", "section"):
            if not item.get(field):
                self.fail(where, f"has no {field}")
        self.text_fields(item, where)
        self.blocks(item.get("detail"), f"{where}.detail")
        if "extra" in item:
            self.extra(item["extra"], f"{where}.extra")

        if kind == "number":
            low, high = item.get("min"), item.get("max")
            if low is None or high is None or low >= high:
                self.fail(where, "a number question needs min below max")
            if "options" in item:
                self.fail(where, "a number question takes min and max, not options")
            pick = item.get("recommend")
            if pick is not None and low is not None and high is not None and not low <= pick <= high:
                self.fail(where, f"recommend {pick} is outside {low} to {high}")
            return

        labels = self.options(item, where, in_batch=kind == "batch")
        if kind == "rank":
            if not 2 <= len(labels) <= 10:
                self.fail(where, "a ranking takes 2 to 10 options")
            pick = item.get("recommend")
            if pick is not None and sorted(pick) != sorted(labels):
                self.fail(where, "a ranking's recommend must list every option label once")
        elif kind == "bracket":
            if not 4 <= len(labels) <= 32:
                self.fail(where, "a bracket takes 4 to 32 options")
            self.recommend(item, labels, where)
        elif kind == "batch":
            if "recommend" in item:
                self.fail(where, "a batch puts recommend on each row, not on the question")
            rows = item.get("items") or []
            if not rows:
                self.fail(where, "a batch has no items")
            row_ids = [row.get("id") for row in rows]
            if len(set(row_ids)) != len(row_ids):
                self.fail(where, "repeats a row id")
            for row in rows:
                self.recommend(row, labels, f"{where}.items[{row.get('id')}]")
        else:
            self.recommend(item, labels, where)

        followups = item.get("followups") or []
        if followups and kind:
            self.fail(where, "only single questions take follow-ups")
        for followup in followups:
            fwhere = f"{where}.followups[{followup.get('id')}]"
            ids.append(followup.get("id"))
            self.text_fields(followup, fwhere, needs_title=False)
            for opener in followup.get("when", []):
                if opener not in labels:
                    self.fail(fwhere, f"when {opener!r} names no option of its question")
            for field in ("extra", "type", "followups"):
                if field in followup:
                    self.fail(fwhere, f"a follow-up takes no {field}")
            self.recommend(followup, self.options(followup, fwhere), fwhere)


def check(data):
    checker = Checker()
    if "round" in data and "questions" not in data:
        data = data["round"]
    config = data.get("config") or {}
    questions = data.get("questions") or []
    if not config.get("title"):
        checker.fail("config", "has no title")
    if not questions:
        checker.fail("round", "has no questions")

    ids = []
    for index, item in enumerate(questions):
        ids.append(item.get("id"))
        checker.question(item, f"questions[{item.get('id', index)}]", ids)
    repeated = sorted({i for i in ids if ids.count(i) > 1 and i})
    if repeated:
        checker.fail("round", f"repeats ids {repeated}")

    needed = (0, 4, 0) if any(q.get("type") in TYPED for q in questions) else (0, 3, 0)
    declared = version(config.get("needs_wizard"))
    if declared is None:
        checker.fail("config", "needs_wizard is missing or not a version")
    elif declared < needed:
        checker.fail("config", f"needs_wizard should be at least {'.'.join(map(str, needed))}")
    if ("project" in config) != ("folder" in config):
        checker.fail("config", "project and folder go together")

    checker.dashes(data, "round")
    return checker.problems


def main():
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2
    with open(sys.argv[1], encoding="utf-8") as handle:
        try:
            data = json.load(handle)
        except json.JSONDecodeError as error:
            print(f"not valid JSON: {error}")
            return 1
    config = (data.get("round") or data).get("config") or {}
    if config.get("kind") == "brainstorm":
        print("skipped: a brainstorm round has its own shape, see references/brainstorms.md")
        return 0
    problems = check(data)
    for problem in problems:
        print(problem)
    if not problems:
        print("ok")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
