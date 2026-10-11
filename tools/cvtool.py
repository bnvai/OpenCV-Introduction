"""Small helper for the learning log.

    python tools/cvtool.py new 2     # create notebook from template for lesson 2
    python tools/cvtool.py sync      # refresh progress table (README) + mindmap (ROADMAP)

Lesson status lives in each notebook's metadata: {"cvintro": {"status": "todo|in-progress|done"}}.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKS = ROOT / "notebooks"
ICON = {"todo": "⬜", "in-progress": "🚧", "done": "✅"}
INDEX_URL = "https://sbirchfield.github.io/cvintro/"


def load_syllabus() -> dict:
    return json.loads((ROOT / "syllabus.json").read_text(encoding="utf-8"))


def slug(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")


def notebook_path(part: dict, lesson: dict) -> Path:
    return NOTEBOOKS / part["dir"] / f"{lesson['n']:02d}_{slug(lesson['title'])}.ipynb"


def read_status(path: Path) -> str:
    if not path.exists():
        return "todo"
    meta = json.loads(path.read_text(encoding="utf-8")).get("metadata", {})
    return meta.get("cvintro", {}).get("status", "in-progress")


def md(text: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": text.strip("\n").splitlines(True)}


def code(text: str) -> dict:
    return {"cell_type": "code", "metadata": {}, "execution_count": None,
            "outputs": [], "source": text.strip("\n").splitlines(True)}


def template_cells(part: dict, lesson: dict) -> list[dict]:
    url = lesson.get("url", INDEX_URL)
    return [
        md(f"# Lesson {lesson['n']:02d} - {lesson['title']}\n\n"
           f"**Part {part['id']}:** {part['title']} ({part['years']})  \n"
           f"**Source:** [{url}]({url})  \n"
           f"**Status:** in-progress"),
        md("## Goals\n- [ ] \n- [ ] "),
        md("## Notes (in my own words)\n\n"),
        code("import numpy as np\nimport cv2\nimport matplotlib.pyplot as plt"),
        md("## Experiments\n\n"),
        code("# build / reproduce the lesson here"),
        md("## My own twist\nSomething beyond the lesson: a different image, a parameter sweep, "
           "a comparison with another method.\n"),
        code("# extension"),
        md("## Takeaways\n- \n\n## Where this shows up in real work\n- "),
    ]


def write_notebook(part: dict, lesson: dict, cells: list[dict], status: str = "in-progress") -> Path:
    path = notebook_path(part, lesson)
    path.parent.mkdir(parents=True, exist_ok=True)
    nb = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python"},
            "cvintro": {"lesson": lesson["n"], "status": status},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def find(syllabus: dict, n: int) -> tuple[dict, dict]:
    for part in syllabus["parts"]:
        for lesson in part["lessons"]:
            if lesson["n"] == n:
                return part, lesson
    raise SystemExit(f"No lesson {n} in syllabus.json")


def replace_block(path: Path, name: str, body: str) -> None:
    start, end = f"<!-- {name}:start -->", f"<!-- {name}:end -->"
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pattern.search(text):
        raise SystemExit(f"Marker {name} missing in {path.name}")
    path.write_text(pattern.sub(lambda _: f"{start}\n{body}\n{end}", text), encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix().replace(" ", "%20")


def sync() -> None:
    syl = load_syllabus()
    total = done = active = 0
    rows, mind = [], ["```mermaid", "mindmap", "  root((OpenCV Intro))"]
    for part in syl["parts"]:
        mind.append(f"    Part {part['id']}: {part['title']}")
        rows += [f"\n### Part {part['id']} - {part['title']} ({part['years']})\n",
                 "| # | Lesson | Status | Notebook |", "|--:|---|:-:|---|"]
        for lesson in part["lessons"]:
            path = notebook_path(part, lesson)
            status = read_status(path)
            total += 1
            done += status == "done"
            active += status == "in-progress"
            link = f"[open]({rel(path)})" if path.exists() else "-"
            rows.append(f"| {lesson['n']:02d} | {lesson['title']} | {ICON[status]} | {link} |")
            label = re.sub(r"[()\[\]{}]", "", lesson["title"])
            mind.append(f"      {ICON[status]} {lesson['n']:02d} {label}")
    mind.append("```")
    summary = (f"**Progress: {done}/{total} lessons done** "
               f"({active} in progress) - {100 * done // total}%")
    replace_block(ROOT / "README.md", "progress", summary + "\n" + "\n".join(rows))
    replace_block(ROOT / "ROADMAP.md", "mindmap", "\n".join(mind))
    print(f"synced: {done}/{total} done, {active} in progress")


def main(argv: list[str]) -> None:
    if argv[:1] == ["sync"]:
        sync()
    elif argv[:1] == ["new"] and len(argv) == 2:
        part, lesson = find(load_syllabus(), int(argv[1]))
        path = notebook_path(part, lesson)
        if path.exists():
            raise SystemExit(f"{path} already exists")
        write_notebook(part, lesson, template_cells(part, lesson))
        print(f"created {path.relative_to(ROOT)}")
        sync()
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
