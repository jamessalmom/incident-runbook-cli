"""Command-line entrypoint: `python -m runbook_cli.cli render path/to/runbook.yaml`."""

from __future__ import annotations

import argparse
import sys

from .runbook import load_runbook, render_markdown


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="runbook", description="Render a YAML runbook to Markdown")
    subparsers = parser.add_subparsers(dest="command", required=True)

    render_parser = subparsers.add_parser("render", help="Render a runbook YAML file to Markdown")
    render_parser.add_argument("path")

    args = parser.parse_args(argv)

    if args.command == "render":
        runbook = load_runbook(args.path)
        print(render_markdown(runbook))
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
