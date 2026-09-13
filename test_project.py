import project
import pytest

def test_add_dummy_transaction():
    with pytest.raises(ValueError):
        transaction = ("", "Income", "test", 390, "description test")
        project.add_dummy_transaction(transaction)
    with pytest.raises(IndexError):
        transaction = ()
        project.add_dummy_transaction(transaction)
