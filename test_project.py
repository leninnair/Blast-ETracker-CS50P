import project
import pytest

def test_add_dummy_transaction():
    with pytest.raises(ValueError):
        transaction = ("", "Income", "test", 390, "description test")
        project.add_dummy_transaction(transaction)
    with pytest.raises(IndexError):
        transaction = ()
        project.add_dummy_transaction(transaction)
    with pytest.raises(ValueError):
        transaction = ("2026-09-10", "Income", "cat1", "abc", "")
        project.add_dummy_transaction(transaction)

def test_fetch_trans():
    assert project.fetch_trans() is not None

def test_delete_trans():
    transaction = ("2026-09-10", "Expense", "Test", 9999, "Test transaction to delete.")
    project.add_dummy_transaction(transaction)
    project.delete_trans(9999)
    transactions = list(project.expenses.data_generator())
    assert not any(transaction[3] == 9999 for transaction in transactions)
