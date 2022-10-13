import pytest
from banking.account import Account, AccountStatus, InsufficientBalanceError, CheckingAccount

test_failure_amounts = [
    (0), (-0.1), (-1)
]

test_success_amounts = [
    (0.1, 1000.1), (1, 1001), (100, 1100)
]


@pytest.fixture
def an_active_account():
    return Account("TR1", 1000, AccountStatus.ACTIVE)


@pytest.fixture
def a_closed_account():
    return Account("TR2", 1000, AccountStatus.CLOSED)


@pytest.mark.parametrize("amount", test_failure_amounts)
def test_deposit_with_zero_amount_should_raise_error(an_active_account, amount):  # 1. test fixture
    with pytest.raises(ValueError):  # 3. verification
        an_active_account.deposit(amount)  # 2. call exercise method
    # 4. test teardown


@pytest.mark.parametrize("amount,expected", test_success_amounts)
def test_deposit_with_positive_amount_should_success(an_active_account, amount, expected):  # 1. test fixture
    an_active_account.deposit(amount)  # 2. call exercise method
    assert an_active_account.balance == expected
    # 4. test teardown


def test_withdraw_with_zero_amount_should_raise_error(an_active_account):  # 1. test fixture
    with pytest.raises(ValueError):  # 3. verification
        an_active_account.withdraw(0.0)  # 2. call exercise method
    # 4. test teardown


def test_withdraw_with_over_balance_should_raise_error(an_active_account):  # 1. test fixture
    with pytest.raises(InsufficientBalanceError):  # 3. verification
        an_active_account.withdraw(1001)  # 2. call exercise method
    # 4. test teardown


def test_withdraw_all_balance_should_success(an_active_account):  # 1. test fixture
    an_active_account.withdraw(1000)  # 2. call exercise method
    assert an_active_account.balance == 0
    # 4. test teardown
