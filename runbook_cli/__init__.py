"""runbook_cli

A tiny CLI + library for keeping incident runbooks as structured YAML
(not scattered wiki pages) and rendering them to Markdown, plus a simple
SQL-anomaly-flagging helper for the kind of window-function checks used
during transaction incident triage.

Built out of the habit of documenting response steps for a mission-
critical payments integration, where "where's the runbook for this
alert" needs to be a fast answer.
"""

from .anomaly import flag_amount_outliers
from .runbook import Runbook, load_runbook, render_markdown

__all__ = ["Runbook", "flag_amount_outliers", "load_runbook", "render_markdown"]
__version__ = "0.1.0"
