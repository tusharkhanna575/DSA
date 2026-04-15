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
    """
    Read the existing README (if any) and reuse:
      - Target
      - Start Date
    so they are not overwritten every run.
    """
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
    dirs: list[Path] = []
    for p in sorted(root.iterdir(), key=lambda x: natural_sort_key(x.name)):
        if (
            p.is_dir()
            and p.name not in EXCLUDED_TOP_LEVEL
            and not p.name.startswith(".")
        ):
            if any(p.rglob("*.py")):
                dirs.append(p)
    return dirs


def count_py_files(folder: Path) -> int:
    return sum(1 for _ in folder.rglob("*.py"))


# ---------------------------------------------------------------------------
# Breadcrumb-style tree emission
# ---------------------------------------------------------------------------

def breadcrumb_for(path: Path, base: Path) -> str:
    """
    Convert a file path into a breadcrumb like:
      Array / Easy / Two Sum
    based on the relative path to `base`.
    """
    rel = path.relative_to(base)
    parts = list(rel.parts)
    if not parts:
        return ""
    # Last part is the filename; use stem without extension
    *dirs, filename = parts
    name = Path(filename).stem
    breadcrumb_parts = [display_name(p) for p in dirs] + [display_name(name)]
    return " / ".join(breadcrumb_parts)


def emit_topic_files_as_breadcrumbs(topic: Path, base: Path) -> list[str]:
    """
    For a given top-level topic folder, list all .py files in
    a nicely sorted, breadcrumb-style bullet list.
    """
    lines: list[str] = []
    py_files = sorted(topic.rglob("*.py"),
                      key=lambda p: natural_sort_key(str(p)))
    if not py_files:
        lines.append("_No problems yet in this topic._")
        return lines

    for py in py_files:
        rel = py.relative_to(base)
        link = encode_link(rel)
        breadcrumb = breadcrumb_for(py, base)
        # Markdown checkbox + breadcrumb as link text
        lines.append(f"- [ ] [{breadcrumb}]({link})")
    return lines


# ---------------------------------------------------------------------------
# Attractive README builder
# ---------------------------------------------------------------------------

def build_readme(existing: str) -> str:
    target, start_date = parse_existing_metadata(existing)
    topics = collect_top_level_dirs(REPO_ROOT)
    topic_counts = [(display_name(topic.name), count_py_files(topic))
                    for topic in topics]
    total = sum(c for _, c in topic_counts)

    lines: list[str] = []

    # Title and hero section
    lines.append("# 📚 DSA Problem Tracker")
    lines.append("")
    lines.append(f"**Target:** {target}")
    lines.append("")
    lines.append(f"**Start Date:** {start_date}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Overview / how to use
    lines.append("## 👀 Overview")
    lines.append("")
    lines.append(
        "This repository is a **topic‑wise DSA practice tracker**. "
        "Each problem is a Python file, grouped by topic and difficulty. "
        "Use the checklist below to track what you've solved."
    )
    lines.append("")
    lines.append("**How to use this tracker:**")
    lines.append("")
    lines.append("1. Pick a topic from the table or list below.")
    lines.append(
        "2. Open a problem link – each one goes directly to the solution file.")
    lines.append(
        "3. After solving/understanding it, replace `[ ]` with `[x]` in the README.")
    lines.append(
        "4. Commit the updated README to record your progress over time.")
    lines.append("")
    lines.append(
        "> Tip: The breadcrumb style links (e.g. `Array / Easy / Two Sum`) ")
    lines.append(
        "> make it easy to understand the topic and sub‑topic at a glance.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Quick stats
    lines.append("## 📊 Progress Snapshot")
    lines.append("")
    lines.append("| Topic | Problems |")
    lines.append("| --- | ---: |")
    for topic_name, count in topic_counts:
        lines.append(f"| {topic_name} | {count} |")
    lines.append(f"| **Total** | **{total}** |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Topic sections with details + breadcrumbs
    lines.append("## 🧭 Topic-wise Navigator")
    lines.append("")
    lines.append(
        "Click on a topic below to expand its problems. "
        "Each item is shown as a breadcrumb like `Topic / Subtopic / ProblemName`."
    )
    lines.append("")

    for topic in topics:
        topic_name = display_name(topic.name)
        topic_count = count_py_files(topic)

        lines.append("<details>")
        lines.append(f"<summary><strong>{topic_name}</strong> &nbsp; "
                     f"<sub>({topic_count} problems)</sub></summary>")
        lines.append("")
        # Optional short description placeholder per topic
        lines.append(f"> _Notes for **{topic_name}**:_ "
                     f"add a short description or strategy tips for this topic here.")
        lines.append("")
        lines.extend(emit_topic_files_as_breadcrumbs(topic, REPO_ROOT))
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
