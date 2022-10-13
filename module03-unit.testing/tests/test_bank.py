import pytest

from banking.bank import Bank
from banking.account import Account

customers = [
    ("1", "jack bauer")
]


@pytest.fixture
def a_bank():
    return Bank("Garanti BBVA")


@pytest.mark.parametrize("identity,fullname", customers)
def test_create_customer_is_success(a_bank, identity, fullname):
    jack = a_bank.create_customer(identity, fullname)
    assert jack.fullname == fullname
    assert jack.identity == identity
    assert len(a_bank.customers) == 1


def test_get_customer_account_is_success(a_bank, mocker):
    jack = a_bank.create_customer("1", "jack bauer")
    account = Account("TR1", 1000)
    mocker.patch('banking.bank.Customer.get_account', return_value=account)
    assert a_bank.get_account("TR1") == account
