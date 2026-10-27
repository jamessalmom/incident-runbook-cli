# incident-runbook-cli

Keeps incident runbooks as YAML files next to the code instead of scattered wiki pages, and renders them to Markdown when needed. It also has a small statistical helper to flag outlier transaction amounts, the kind of quick check that helps when investigating anomalies in high-volume payment flows.

## Why YAML

A wiki page goes out of date without anyone noticing. A YAML file in the repository is reviewed in the same pull request as the alert it describes, shows clean diffs, and can be validated in CI.

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

Flagging outliers:

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

MIT, see [LICENSE](LICENSE).
