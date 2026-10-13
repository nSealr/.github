#!/usr/bin/env python3
"""Verify the nSealr organization metadata repository."""

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
    ".github/pull_request_template.md",
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
    label_names: set[str] = set()
    area_labels: set[str] = set()
    if labels_path.exists():
        parsed = yaml.safe_load(labels_path.read_text(encoding="utf-8"))
        names = [entry.get("name") for entry in parsed.get("labels", [])]
        label_names = {name for name in names if isinstance(name, str)}
        if len(names) != len(label_names):
            errors.append("duplicate label names")
        for required in ("type:security", "priority:p0"):
            if required not in label_names:
                errors.append(f"missing required label: {required}")
        area_labels = {
            name.removeprefix("area:")
            for name in label_names
            if name.startswith("area:")
        }
        if not area_labels:
            errors.append("at least one area label is required")

    template_dir = ROOT / ".github" / "ISSUE_TEMPLATE"
    if label_names and template_dir.exists():
        for template_path in sorted(template_dir.glob("*.yml")):
            if template_path.name == "config.yml":
                continue
            parsed = yaml.safe_load(template_path.read_text(encoding="utf-8"))
            for label in parsed.get("labels", []):
                if label not in label_names:
                    errors.append(
                        f"{template_path.relative_to(ROOT)} references unknown label: {label}"
                    )

    feature_template = ROOT / ".github" / "ISSUE_TEMPLATE" / "feature_request.yml"
    if feature_template.exists():
        parsed = yaml.safe_load(feature_template.read_text(encoding="utf-8"))
        areas: set[str] = set()
        for item in parsed.get("body", []):
            if item.get("id") == "area":
                areas = set(item.get("attributes", {}).get("options", []))
        if areas != area_labels:
            errors.append(
                "feature request area options must match declared area labels: "
                + ", ".join(sorted(area_labels))
            )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("nSealr organization metadata verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
