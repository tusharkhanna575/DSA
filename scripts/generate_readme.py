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
CHECKBOX_LINE_RE = re.compile(r"^- \[( |x|X)\] \[[^\]]+\]\(([^)]+)\)$")


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


def parse_existing_check_states(readme_text: str) -> dict[str, bool]:
    """Reuse checkbox state from the previous README generation."""
    states: dict[str, bool] = {}

    for line in readme_text.splitlines():
        match = CHECKBOX_LINE_RE.match(line.strip())
        if match:
            states[match.group(2)] = match.group(1).lower() == "x"

    return states


def build_topic_tree(topic: Path) -> dict[str, object]:
    tree: dict[str, object] = {"children": {}, "files": []}

    py_files = sorted(
        topic.rglob("*.py"),
        key=lambda p: natural_sort_key(p.relative_to(topic).as_posix()),
    )

    for py in py_files:
        rel_parts = py.relative_to(topic).parts
        node = tree

        for folder in rel_parts[:-1]:
            children = node["children"]  # type: ignore[index]
            # type: ignore[assignment]
            node = children.setdefault(folder, {"children": {}, "files": []})

        node["files"].append(py)  # type: ignore[index]

    return tree


def node_total(node: dict[str, object]) -> int:
    files = node["files"]  # type: ignore[index]
    children = node["children"]  # type: ignore[index]
    return len(files) + sum(node_total(child) for child in children.values())


def node_solved(node: dict[str, object], status_map: dict[str, bool], base: Path) -> int:
    solved = 0

    for py in node["files"]:  # type: ignore[index]
        rel = encode_link(py.relative_to(base))
        if status_map.get(rel, False):
            solved += 1

    for child in node["children"].values():  # type: ignore[index]
        solved += node_solved(child, status_map, base)

    return solved


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


def emit_file_list(
    files: list[Path],
    base: Path,
    status_map: dict[str, bool],
    prefix: str = "",
) -> list[str]:
    lines: list[str] = []
    for py in files:
        rel = py.relative_to(base)
        link = encode_link(rel)
        breadcrumb = breadcrumb_for(py, base)
        checked = "x" if status_map.get(link, False) else " "
        lines.append(f"{prefix}- [{checked}] [{breadcrumb}]({link})")
    return lines


def emit_tree_node(
    node: dict[str, object],
    base: Path,
    status_map: dict[str, bool],
    label: str | None = None,
    depth: int = 0,
) -> list[str]:
    lines: list[str] = []
    total = node_total(node)
    solved = node_solved(node, status_map, base)
    children = node["children"]  # type: ignore[index]
    files = node["files"]  # type: ignore[index]
    indent = "  " * depth
    file_indent = indent + "  "

    if label is not None:
        if depth == 0:
            lines.append(f"{indent}<details>")
            lines.append(
                f"{indent}<summary><strong>{label}</strong> &nbsp; <sub>({solved}/{total} solved)</sub></summary>"
            )
            lines.append("")
        else:
            lines.append(f"{indent}- <details>")
            lines.append(
                f"{indent}  <summary><strong>{label}</strong> &nbsp; <sub>({solved}/{total} solved)</sub></summary>"
            )
            lines.append("")

    if files:
        lines.extend(emit_file_list(files, base, status_map,
                     prefix=file_indent if label is not None else ""))
        if label is not None:
            lines.append("")

    for child_name in sorted(children, key=natural_sort_key):
        child = children[child_name]
        lines.extend(
            emit_tree_node(
                child,
                base,
                status_map,
                display_name(child_name),
                depth=depth + 1,
            )
        )
        lines.append("")

    if label is not None:
        lines.append(f"{indent}</details>")

    return lines


# ---------------------------------------------------------------------------
# Attractive README builder
# ---------------------------------------------------------------------------

def build_readme(existing: str) -> str:
    target, start_date = parse_existing_metadata(existing)
    status_map = parse_existing_check_states(existing)
    topics = collect_top_level_dirs(REPO_ROOT)

    topic_stats: list[tuple[str, int, int, int]] = []
    solved_total = 0
    total = 0

    for topic in topics:
        tree = build_topic_tree(topic)
        topic_total = node_total(tree)
        topic_solved = node_solved(tree, status_map, REPO_ROOT)
        topic_stats.append(
            (display_name(topic.name), topic_solved, topic_total,
             len(tree["children"]))  # type: ignore[index]
        )
        solved_total += topic_solved
        total += topic_total

    remaining = total - solved_total
    completion = (solved_total / total * 100) if total else 0.0

    lines: list[str] = []

    # Title and hero section
    lines.append("# 📚 DSA Problem Tracker")
    lines.append("")
    lines.append(f"**Target:** {target}")
    lines.append("")
    lines.append(f"**Start Date:** {start_date}")
    lines.append("")
    lines.append(
        f"> Progress: **{solved_total}/{total} solved** · **{remaining} remaining** · **{completion:.1f}% complete**"
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    # Overview / how to use
    lines.append("## 👀 Overview")
    lines.append("")
    lines.append(
        "This repository is a **topic‑wise DSA practice tracker**. "
        "Each problem is a Python file, grouped by topic, subtopic, and folder depth. "
        "Use the checklist below to track what you've solved and keep the hierarchy readable."
    )
    lines.append("")
    lines.append("**How to use this tracker:**")
    lines.append("")
    lines.append("1. Pick a topic from the progress table or navigator below.")
    lines.append(
        "2. Follow the nested topic -> subtopic -> problem path to find the file quickly.")
    lines.append(
        "3. After solving or revisiting it, tick the checkbox so the next README generation preserves it.")
    lines.append(
        "4. Commit the updated README to record your progress over time.")
    lines.append("")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Quick stats
    lines.append("## 📊 Progress Snapshot")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("| --- | ---: |")
    lines.append(f"| Completed | {solved_total} |")
    lines.append(f"| Remaining | {remaining} |")
    lines.append(f"| Total | {total} |")
    lines.append("")
    lines.append("| Topic | Problems |")
    lines.append("| --- | ---: |")
    for topic_name, solved, count, _folder_count in topic_stats:
        lines.append(f"| {topic_name} | {solved}/{count} |")
    lines.append(f"| **Total** | **{solved_total}/{total}** |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Topic sections with details + breadcrumbs
    lines.append("## 🧭 Topic-wise Navigator")
    lines.append("")
    lines.append(
        "Click on a topic below to expand its folder tree. "
        "Subtopics and subfolders are grouped explicitly so the structure stays easy to scan."
    )
    lines.append("")

    for topic, (_, solved, count, folder_count) in zip(topics, topic_stats):
        topic_name = display_name(topic.name)
        tree = build_topic_tree(topic)

        lines.append("<details>")
        lines.append(
            f"<summary><strong>{topic_name}</strong> &nbsp; <sub>({solved}/{count} solved · {folder_count} folders)</sub></summary>"
        )
        lines.extend(emit_tree_node(tree, REPO_ROOT, status_map))
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
