"""Structured runbook model: YAML in, Markdown out."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class RunbookStep:
    description: str
    command: str | None = None


@dataclass
class Runbook:
    title: str
    severity: str
    triggers: list[str]
    steps: list[RunbookStep] = field(default_factory=list)
    escalation: str | None = None


def load_runbook(path: str | Path) -> Runbook:
    data = yaml.safe_load(Path(path).read_text())
    steps = [RunbookStep(**s) if isinstance(s, dict) else RunbookStep(description=s) for s in data.get("steps", [])]
    return Runbook(
        title=data["title"],
        severity=data.get("severity", "unknown"),
        triggers=data.get("triggers", []),
        steps=steps,
        escalation=data.get("escalation"),
    )


def render_markdown(runbook: Runbook) -> str:
    lines = [f"# {runbook.title}", "", f"**Severity:** {runbook.severity}", ""]

    if runbook.triggers:
        lines.append("## Triggers")
        lines.extend(f"- {t}" for t in runbook.triggers)
        lines.append("")

    if runbook.steps:
        lines.append("## Response steps")
        for i, step in enumerate(runbook.steps, start=1):
            lines.append(f"{i}. {step.description}")
            if step.command:
                lines.append(f"   ```\n   {step.command}\n   ```")
        lines.append("")

    if runbook.escalation:
        lines.append("## Escalation")
        lines.append(runbook.escalation)
        lines.append("")

    return "\n".join(lines)
