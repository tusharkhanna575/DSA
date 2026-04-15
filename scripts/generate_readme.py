from __future__ import annotations

from pathlib import Path
import re
from urllib.parse import quote


REPO_ROOT = Path(__file__).resolve().parents[1]
README_PATH = REPO_ROOT / "readme.md"

EXCLUDED_TOP_LEVEL = {".git", ".github", "scripts", "__pycache__"}
DISPLAY_NAME_OVERRIDES = {
    "Binary Seach": "Binary Search",
}
NESTED_INDENT = "    "


def parse_existing_metadata(readme_text: str) -> tuple[str, str]:
    target = "Product Based Company"
    start_date = "25 November 2025"

    for line in readme_text.splitlines():
        if line.startswith("Target:"):
            target = line.split(":", 1)[1].strip() or target
        if line.startswith("Start Date:"):
            start_date = line.split(":", 1)[1].strip() or start_date
    return target, start_date


def display_name(name: str) -> str:
    if name in DISPLAY_NAME_OVERRIDES:
        return DISPLAY_NAME_OVERRIDES[name]
    return name


def encode_link(path: Path) -> str:
    return quote(path.as_posix(), safe="/.")


def natural_sort_key(name: str) -> list[object]:
    parts = re.split(r"(\d+)", name)
    key: list[object] = []
    for part in parts:
        if part.isdigit():
            key.append(int(part))
        else:
            key.append(part.lower())
    return key


def collect_top_level_dirs(root: Path) -> list[Path]:
    dirs = []
    for p in sorted(root.iterdir(), key=lambda x: natural_sort_key(x.name)):
        if p.is_dir() and p.name not in EXCLUDED_TOP_LEVEL and not p.name.startswith("."):
            if any(p.rglob("*.py")):
                dirs.append(p)
    return dirs


def count_py_files(folder: Path) -> int:
    return sum(1 for _ in folder.rglob("*.py"))


def emit_tree(folder: Path, base: Path, level: int = 0) -> list[str]:
    lines: list[str] = []
    indent = NESTED_INDENT * level

    subdirs = [
        p
        for p in sorted(folder.iterdir(), key=lambda x: natural_sort_key(x.name))
        if p.is_dir()
    ]
    py_files = [
        p
        for p in sorted(folder.iterdir(), key=lambda x: natural_sort_key(x.name))
        if p.is_file() and p.suffix == ".py"
    ]

    for subdir in subdirs:
        if not any(subdir.rglob("*.py")):
            continue
        lines.append(f"{indent}<details>")
        lines.append(
            f"{indent}<summary><strong>{display_name(subdir.name)}</strong></summary>")
        lines.append("")
        lines.extend(emit_tree(subdir, base, level + 1))
        lines.append(f"{indent}</details>")
        lines.append("")

    for py in py_files:
        rel = py.relative_to(base)
        name = py.stem
        lines.append(f"{indent}- [ ] [{name}]({encode_link(rel)})")

    return lines


def build_readme(existing: str) -> str:
    target, start_date = parse_existing_metadata(existing)
    topics = collect_top_level_dirs(REPO_ROOT)
    topic_counts = [(display_name(topic.name), count_py_files(topic))
                    for topic in topics]
    total = sum(c for _, c in topic_counts)

    lines: list[str] = []
    lines.append("# DSA Problem Tracker")
    lines.append("")
    lines.append(f"Target: {target}")
    lines.append("")
    lines.append(f"Start Date: {start_date}")
    lines.append("")
    lines.append("## Overview")
    lines.append("")
    lines.append(
        "This repository is organized as a topic-wise DSA practice tracker. "
        "Every problem below links directly to its solution file, so you can open "
        "the code from the README and mark your progress as you go."
    )
    lines.append("")
    lines.append("## Progress Snapshot")
    lines.append("")
    lines.append("| Topic | Problems |")
    lines.append("| --- | ---: |")
    for topic_name, count in topic_counts:
        lines.append(f"| {topic_name} | {count} |")
    lines.append(f"| Total | {total} |")
    lines.append("")

    for topic in topics:
        lines.append("<details>")
        lines.append(
            f"<summary><strong>{display_name(topic.name)}</strong></summary>")
        lines.append("")
        lines.extend(emit_tree(topic, REPO_ROOT, 0))
        lines.append("")
        lines.append("</details>")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    existing = README_PATH.read_text(
        encoding="utf-8") if README_PATH.exists() else ""
    new_content = build_readme(existing)
    README_PATH.write_text(new_content, encoding="utf-8")


if __name__ == "__main__":
    main()
