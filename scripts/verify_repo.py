#!/usr/bin/env python3
"""Verify the NostrSeal organization metadata repository."""

from __future__ import annotations

from pathlib import Path
import sys
import yaml


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    ".pre-commit-config.yaml",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "profile/README.md",
    "docs/audit-loop.md",
    "docs/license-policy.md",
    "docs/superpowers-workflow.md",
    ".github/labels.yml",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/ISSUE_TEMPLATE/research_task.yml",
    ".github/ISSUE_TEMPLATE/hardware_validation.yml",
    ".github/ISSUE_TEMPLATE/security_review.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
]


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing required file: {rel}")
        elif path.is_file() and not path.read_text(encoding="utf-8").strip():
            errors.append(f"empty required file: {rel}")

    labels_path = ROOT / ".github" / "labels.yml"
    if labels_path.exists():
        parsed = yaml.safe_load(labels_path.read_text(encoding="utf-8"))
        names = [entry.get("name") for entry in parsed.get("labels", [])]
        for required in ("area:specs", "type:security", "priority:p0"):
            if required not in names:
                errors.append(f"missing required label: {required}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("NostrSeal organization metadata verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
