from pathlib import Path

from runbook_cli.runbook import load_runbook, render_markdown

FIXTURE = Path(__file__).parent.parent / "runbook_cli" / "templates" / "example_runbook.yaml"


def test_loads_runbook_from_yaml():
    runbook = load_runbook(FIXTURE)
    assert runbook.title == "PIX settlement latency spike"
    assert runbook.severity == "high"
    assert len(runbook.steps) == 4


def test_renders_markdown_with_expected_sections():
    runbook = load_runbook(FIXTURE)
    markdown = render_markdown(runbook)
    assert "# PIX settlement latency spike" in markdown
    assert "## Triggers" in markdown
    assert "## Response steps" in markdown
    assert "## Escalation" in markdown
    assert "git log" in markdown
