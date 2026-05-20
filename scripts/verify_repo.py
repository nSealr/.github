#!/usr/bin/env python3
"""Verify the nSealr organization metadata repository."""

from __future__ import annotations

from pathlib import Path
import subprocess
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

FORBIDDEN_CURRENT_TERMS = {
    "Nostr" + "Seal",
    "nostr" + "seal",
    "nsealr" + "/vault",
    "nostr" + "seal/vault",
}

REQUIRED_PR_AUDIT_STRINGS = {
    "five-signer-family taxonomy",
    "companion/browser/SDK path stays secretless",
    "QR vault behavior remains stateless",
    "ESP32 production signing remains disabled",
    "Smartcard review remains display-less",
    "TROPIC01 direct BIP-340/Schnorr support is not claimed",
    "No stale, legacy, or duplicate implementation path",
}


def tracked_text_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [ROOT / rel for rel in sorted(result.stdout.splitlines())]


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
    if labels_path.exists():
        parsed = yaml.safe_load(labels_path.read_text(encoding="utf-8"))
        names = [entry.get("name") for entry in parsed.get("labels", [])]
        label_names = {name for name in names if isinstance(name, str)}
        for required in ("area:specs", "area:raspberry", "type:security", "priority:p0"):
            if required not in label_names:
                errors.append(f"missing required label: {required}")
        for label in sorted(CANONICAL_AREA_LABELS):
            if label not in label_names:
                errors.append(f"missing canonical area label: {label}")
        area_labels = {
            name.removeprefix("area:")
            for name in label_names
            if name.startswith("area:")
        }
        if area_labels != CANONICAL_FEATURE_AREAS:
            errors.append(
                "area labels must match canonical repositories: "
                + ", ".join(sorted(CANONICAL_FEATURE_AREAS))
            )

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

    pr_template = ROOT / ".github" / "pull_request_template.md"
    if pr_template.exists():
        pr_text = pr_template.read_text(encoding="utf-8")
        for required in sorted(REQUIRED_PR_AUDIT_STRINGS):
            if required not in pr_text:
                errors.append(f"pull request template missing audit gate: {required}")

    for path in tracked_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for term in sorted(FORBIDDEN_CURRENT_TERMS):
            if term in text:
                errors.append(f"{path.relative_to(ROOT)} contains stale term: {term}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("nSealr organization metadata verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
