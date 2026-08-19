"""Simple statistical outlier flagging for transaction amounts.

A lightweight, dependency-free stand-in for the kind of window-function
SQL check ("amount more than N standard deviations from the recent
average") used to triage anomalies in high-volume transaction data.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from statistics import mean, pstdev


@dataclass(frozen=True)
class Transaction:
    tx_id: str
    amount: float


@dataclass(frozen=True)
class FlaggedTransaction:
    tx_id: str
    amount: float
    z_score: float


def flag_amount_outliers(
    transactions: Sequence[Transaction], z_threshold: float = 3.0
) -> list[FlaggedTransaction]:
    if len(transactions) < 2:
        return []

    amounts = [t.amount for t in transactions]
    avg = mean(amounts)
    std_dev = pstdev(amounts)
    if std_dev == 0:
        return []

    flagged = []
    for t in transactions:
        z = (t.amount - avg) / std_dev
        if abs(z) >= z_threshold:
            flagged.append(FlaggedTransaction(tx_id=t.tx_id, amount=t.amount, z_score=round(z, 2)))
    return flagged
