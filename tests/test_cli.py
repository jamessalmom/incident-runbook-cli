from pathlib import Path

from runbook_cli.cli import main

FIXTURE = Path(__file__).parent.parent / "runbook_cli" / "templates" / "example_runbook.yaml"


def test_render_command_prints_markdown(capsys):
    exit_code = main(["render", str(FIXTURE)])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "# PIX settlement latency spike" in captured.out
