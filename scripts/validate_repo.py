from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "Makefile",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/taxonomy_task.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/ci.yml",
    "docs/README.md",
    "docs/evidence-handoff.md",
    "figures/README.md",
    "scripts/validate_repo.py",
    "taxonomy/README.md",
    "taxonomy/agent-layer.md",
    "taxonomy/evaluation-layer.md",
    "taxonomy/glossary.md",
    "taxonomy/governance-layer.md",
    "taxonomy/inference-layer.md",
    "taxonomy/memory-layer.md",
    "taxonomy/model-layer.md",
    "taxonomy/retrieval-layer.md",
    "taxonomy/training-layer.md",
    "tests/README.md",
]

REQUIRED_DIRECTORIES = [
    ".github",
    ".github/ISSUE_TEMPLATE",
    ".github/workflows",
    "docs",
    "figures",
    "scripts",
    "taxonomy",
    "tests",
]

SECRET_PATTERNS = [
    re.compile(pattern)
    for pattern in [
        r"AKIA[0-9A-Z]{16}",
        r"gho_[A-Za-z0-9_]+",
        r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----",
        r"(?i)\b(password|secret|token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{12,}",
    ]
]

FOUNDATION_MARKERS = {
    "taxonomy/README.md": [
        "# Taxonomy",
        "## Taxonomy Skeleton",
        "## Layer Stubs",
        "## Current Limits",
    ],
    "docs/evidence-handoff.md": [
        "# Evidence Handoff",
        "## Handoff Requirements",
        "## Readiness States",
        "## Current Limits",
    ],
    "taxonomy/glossary.md": [
        "# Glossary",
        "## Future Entry Shape",
        "## Current Entries",
        "## Current Limits",
    ],
}

LAYER_STUB_FILES = [
    "taxonomy/agent-layer.md",
    "taxonomy/evaluation-layer.md",
    "taxonomy/governance-layer.md",
    "taxonomy/inference-layer.md",
    "taxonomy/memory-layer.md",
    "taxonomy/model-layer.md",
    "taxonomy/retrieval-layer.md",
    "taxonomy/training-layer.md",
]


def fail(message: str) -> None:
    raise SystemExit(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def iter_text_files() -> list[Path]:
    excluded_parts = {".git", "__pycache__"}
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if excluded_parts.intersection(path.parts):
            continue
        if path.suffix.lower() in {".md", ".yml", ".yaml", ".py", ""}:
            files.append(path)
    return files


def validate_required_paths() -> None:
    missing_files = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    missing_dirs = [path for path in REQUIRED_DIRECTORIES if not (ROOT / path).is_dir()]
    if missing_files or missing_dirs:
        details = []
        if missing_files:
            details.append("missing files: " + ", ".join(missing_files))
        if missing_dirs:
            details.append("missing directories: " + ", ".join(missing_dirs))
        fail("; ".join(details))


def validate_foundation_markers() -> None:
    for relative_path, markers in FOUNDATION_MARKERS.items():
        text = read_text(ROOT / relative_path)
        missing_markers = [marker for marker in markers if marker not in text]
        if missing_markers:
            fail(
                f"{relative_path} is missing expected marker(s): "
                + ", ".join(missing_markers)
            )


def validate_layer_stubs() -> None:
    required_markers = [
        "Draft status: Not drafted.",
        "Purpose:",
        "Evidence requirement:",
        "## Boundary Descriptions",
        "## Architecture Diagram",
        "```mermaid",
    ]
    for relative_path in LAYER_STUB_FILES:
        text = read_text(ROOT / relative_path)
        missing_markers = [marker for marker in required_markers if marker not in text]
        if missing_markers:
            fail(
                f"{relative_path} is missing expected marker(s): "
                + ", ".join(missing_markers)
            )


def validate_glossary_entries() -> None:
    text = read_text(ROOT / "taxonomy/glossary.md")
    allowed_states = {"planning", "evidence_needed", "candidate", "ready", "blocked"}
    allowed_layers = {
        "Model Layer",
        "Training Layer",
        "Inference Layer",
        "Retrieval Layer",
        "Memory Layer",
        "Agent Layer",
        "Evaluation Layer",
        "Governance Layer",
    }
    
    rows = []
    for line in text.splitlines():
        if line.startswith("|") and not line.startswith("|---"):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 5 and parts[0] != "Term":
                rows.append(parts)
                
    if not rows:
        fail("taxonomy/glossary.md must contain at least one glossary entry.")
        
    for row in rows:
        term, layer, state_raw, claim, source = row[0], row[1], row[2], row[3], row[4]
        state = state_raw.replace("`", "")
        
        if layer not in allowed_layers:
            fail(f"Invalid layer '{layer}' for term '{term}' in glossary.md")
        if state not in allowed_states:
            fail(f"Invalid readiness state '{state}' for term '{term}' in glossary.md")
        
        if claim != "N/A" and not re.match(r"^claim-\d+$", claim):
            fail(f"Invalid Claim ID format '{claim}' for term '{term}' in glossary.md")
            
        if source != "N/A" and not re.match(r"^source-[A-Za-z0-9_\-]+$", source):
            fail(f"Invalid Source ID format '{source}' for term '{term}' in glossary.md")


def validate_sub_layer_components() -> None:
    # Validate agent-layer sub-components
    agent_text = read_text(ROOT / "taxonomy/agent-layer.md")
    required_agent_markers = [
        "## Sub-layer Components",
        "* **Planner**:",
        "* **Tool Executors**:",
        "* **Trace**:",
    ]
    for marker in required_agent_markers:
        if marker not in agent_text:
            fail(f"taxonomy/agent-layer.md is missing expected sub-layer marker: {marker}")

    # Validate memory-layer sub-components
    memory_text = read_text(ROOT / "taxonomy/memory-layer.md")
    required_memory_markers = [
        "## Sub-layer Components",
        "* **Short-term Cache**:",
        "* **Episodic Cache**:",
        "* **Long-term Cache**:",
    ]
    for marker in required_memory_markers:
        if marker not in memory_text:
            fail(f"taxonomy/memory-layer.md is missing expected sub-layer marker: {marker}")


def lint_text() -> None:
    for path in iter_text_files():
        text = read_text(path)
        relative = path.relative_to(ROOT)
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(f"possible secret in {relative}: {pattern.pattern}")


def run_validate() -> None:
    validate_required_paths()
    validate_foundation_markers()
    validate_layer_stubs()
    validate_sub_layer_components()
    validate_glossary_entries()


def run_lint() -> None:
    lint_text()


def run_test() -> None:
    run_validate()
    run_lint()


def main(argv: list[str]) -> int:
    if len(argv) == 1:
        command = "test"
    elif len(argv) == 2 and argv[1] in {"validate", "lint", "test"}:
        command = argv[1]
    else:
        print("usage: validate_repo.py {validate|lint|test}", file=sys.stderr)
        return 2

    if command == "validate":
        run_validate()
    elif command == "lint":
        run_lint()
    else:
        run_test()

    print(f"{command} ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
