#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import re
import sys
from dataclasses import dataclass
from pathlib import Path


SECTION_HEADER_RE = re.compile(
    r"^## (?P<path>[^\n]+)\n\n"
    r"Dateityp: (?P<dtype>[^\n]+)\n\n"
    r"(?P<fence>(?P<fence_token>[`~]{3,})(?P<info>[^\n]*))\n",
    re.M,
)

DENIED_BUNDLE_PATHS = {
    "email-builder/agent/systemprompt.md",
    "email-builder/agent-upload/email-builder-agent/systemprompt.md",
    "email-builder/agent/preview-styles.css",
}


@dataclass(frozen=True)
class SectionSpec:
    path: str
    dtype: str
    info: str


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def default_bundle_path() -> Path:
    return Path(__file__).resolve().parent / "email-builder-agent" / "emb_knowledge.md"


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_specs(specs: list[SectionSpec]) -> None:
    denied = [spec.path for spec in specs if spec.path in DENIED_BUNDLE_PATHS]
    if denied:
        denied_list = ", ".join(denied)
        raise ValueError(f"Bundle contains denied section path(s): {denied_list}")


def collect_specs(bundle_text: str) -> tuple[str, list[SectionSpec]]:
    matches = list(SECTION_HEADER_RE.finditer(bundle_text))
    if not matches:
      raise ValueError("No bundle sections found.")
    preamble = bundle_text[: matches[0].start()]
    specs = [
        SectionSpec(
            path=match.group("path").strip(),
            dtype=match.group("dtype").strip(),
            info=match.group("info").strip(),
        )
        for match in matches
    ]
    validate_specs(specs)
    return preamble, specs


def choose_fence(body: str) -> str:
    max_backticks = 0
    for match in re.finditer(r"`+", body):
        max_backticks = max(max_backticks, len(match.group(0)))
    return "`" * max(3, max_backticks + 1)


def render_section(root: Path, spec: SectionSpec) -> str:
    src = root / spec.path
    if not src.is_file():
        raise FileNotFoundError(f"Missing source file for bundle section: {spec.path}")
    body = load_text(src)
    if body.endswith("\n"):
        body = body[:-1]
    fence = choose_fence(body)
    info = spec.info or spec.dtype
    return (
        f"## {spec.path}\n\n"
        f"Dateityp: {spec.dtype}\n\n"
        f"{fence}{info}\n"
        f"{body}\n"
        f"{fence}"
    )


def render_bundle(root: Path, bundle_path: Path) -> str:
    current = load_text(bundle_path)
    preamble, specs = collect_specs(current)
    sections = [render_section(root, spec) for spec in specs]
    return preamble.rstrip("\n") + "\n\n" + "\n\n".join(sections) + "\n"


def extract_current_sections(bundle_text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    for match in SECTION_HEADER_RE.finditer(bundle_text):
        path = match.group("path").strip()
        fence_token = match.group("fence_token")
        body_start = match.end()
        closing_re = re.compile(rf"(?m)^{re.escape(fence_token)}\s*$")
        closing = closing_re.search(bundle_text, body_start)
        if not closing:
            continue
        body = bundle_text[body_start:closing.start()]
        if body.endswith("\n"):
            body = body[:-1]
        sections[path] = body
    return sections


def check_bundle(root: Path, bundle_path: Path) -> tuple[bool, list[str]]:
    current = load_text(bundle_path)
    _, specs = collect_specs(current)
    current_sections = extract_current_sections(current)
    changed: list[str] = []
    for spec in specs:
        src_text = load_text(root / spec.path)
        if src_text.endswith("\n"):
            src_text = src_text[:-1]
        if current_sections.get(spec.path) != src_text:
            changed.append(spec.path)
    return len(changed) == 0, changed


def cmd_rebuild(bundle_path: Path) -> int:
    root = repo_root()
    rendered = render_bundle(root, bundle_path)
    bundle_path.write_text(rendered, encoding="utf-8")
    return 0


def cmd_check(bundle_path: Path, verbose: bool) -> int:
    root = repo_root()
    rendered = render_bundle(root, bundle_path)
    current = load_text(bundle_path)
    is_exact = rendered == current
    is_synced, changed = check_bundle(root, bundle_path)
    print(f"bundle_exact={'true' if is_exact else 'false'}")
    print(f"bundle_synced={'true' if is_synced else 'false'}")
    if changed:
        for path in changed:
            print(path)
        print(f"count={len(changed)}")
    if verbose and not is_exact:
        diff = difflib.unified_diff(
            current.splitlines(),
            rendered.splitlines(),
            fromfile="current",
            tofile="rendered",
            lineterm="",
        )
        for line in list(diff)[:200]:
            print(line)
    return 0 if is_exact and is_synced else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Rebuild or check the EMB knowledge bundle.")
    parser.add_argument("command", choices=["rebuild", "check"])
    parser.add_argument(
        "--bundle",
        type=Path,
        default=default_bundle_path(),
        help="Path to emb_knowledge.md",
    )
    parser.add_argument("--verbose", action="store_true", help="Show a diff during check failures.")
    args = parser.parse_args()

    if args.command == "rebuild":
        return cmd_rebuild(args.bundle)
    return cmd_check(args.bundle, args.verbose)


if __name__ == "__main__":
    sys.exit(main())
