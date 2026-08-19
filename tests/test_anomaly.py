from runbook_cli.anomaly import Transaction, flag_amount_outliers


def test_flags_transaction_far_from_the_mean():
    txs = [Transaction(f"t{i}", 100.0) for i in range(10)]
    txs.append(Transaction("outlier", 100_000.0))
    flagged = flag_amount_outliers(txs, z_threshold=3.0)
    assert len(flagged) == 1
    assert flagged[0].tx_id == "outlier"


def test_no_flags_when_all_amounts_are_similar():
    txs = [Transaction(f"t{i}", 100.0 + i) for i in range(10)]
    assert flag_amount_outliers(txs) == []


def test_handles_fewer_than_two_transactions():
    assert flag_amount_outliers([]) == []
    assert flag_amount_outliers([Transaction("t1", 100.0)]) == []
