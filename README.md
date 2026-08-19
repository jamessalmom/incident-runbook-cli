# incident-runbook-cli

Keeps incident runbooks as **structured YAML** instead of scattered wiki
pages, renders them to Markdown on demand, and includes a small
statistical helper for flagging outlier transaction amounts — the kind
of quick triage check used while investigating anomalies in
high-volume, mission-critical transaction data (PIX-style settlement
flows).

## Why structured runbooks

A wiki page drifts out of date silently. A YAML file next to the code
gets reviewed in the same pull request as the alert it documents, diffs
cleanly, and can be rendered/linted in CI.

## Usage

```bash
python -m runbook_cli.cli render runbook_cli/templates/example_runbook.yaml
```

```yaml
title: PIX settlement latency spike
severity: high
triggers:
  - "p99 settlement latency > 5s for 3 consecutive minutes"
steps:
  - description: Confirm the alert against the latency dashboard
  - description: Check recent deploys in the last 30 minutes
    command: "git log --since='30 minutes ago' --oneline"
escalation: "If unresolved in 15 minutes, page the on-call SRE."
```

Outlier flagging:

```python
from runbook_cli.anomaly import Transaction, flag_amount_outliers

flagged = flag_amount_outliers([Transaction("tx1", 100.0), Transaction("tx2", 50000.0)])
```

## Development

```bash
pip install -r requirements.txt
pip install pytest ruff
pytest
ruff check .
```

## License

MIT — see [LICENSE](LICENSE).
