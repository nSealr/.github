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
]

CANONICAL_FEATURE_AREAS = {
    "specs",
    "companion",
    "raspberry",
    "esp32",
    "smartcard",
    "hardware",
    "website",
    "lab",
}

CANONICAL_AREA_LABELS = {f"area:{area}" for area in CANONICAL_FEATURE_AREAS}

CANONICAL_REPOSITORIES = {
    ".github",
    "lab",
    "website",
    "specs",
    "companion",
    "esp32",
    "raspberry",
    "smartcard",
    "hardware",
}


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
        for required in ("area:specs", "area:raspberry", "type:security", "priority:p0"):
            if required not in names:
                errors.append(f"missing required label: {required}")
        for label in sorted(CANONICAL_AREA_LABELS):
            if label not in names:
                errors.append(f"missing canonical area label: {label}")
        area_labels = {
            name.removeprefix("area:")
            for name in names
            if isinstance(name, str) and name.startswith("area:")
        }
        if area_labels != CANONICAL_FEATURE_AREAS:
            errors.append(
                "area labels must match canonical repositories: "
                + ", ".join(sorted(CANONICAL_FEATURE_AREAS))
            )

    feature_template = ROOT / ".github" / "ISSUE_TEMPLATE" / "feature_request.yml"
    if feature_template.exists():
        parsed = yaml.safe_load(feature_template.read_text(encoding="utf-8"))
        areas: set[str] = set()
        for item in parsed.get("body", []):
            if item.get("id") == "area":
                areas = set(item.get("attributes", {}).get("options", []))
        if areas != CANONICAL_FEATURE_AREAS:
            errors.append(
                "feature request area options must match canonical repositories: "
                + ", ".join(sorted(CANONICAL_FEATURE_AREAS))
            )

    profile_path = ROOT / "profile" / "README.md"
    if profile_path.exists():
        profile_repos = set()
        for line in profile_path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if stripped.startswith("- `"):
                profile_repos.add(stripped.split("`", 2)[1])
        if profile_repos != CANONICAL_REPOSITORIES:
            errors.append(
                "profile repository list must match canonical repositories: "
                + ", ".join(sorted(CANONICAL_REPOSITORIES))
            )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("nSealr organization metadata verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
