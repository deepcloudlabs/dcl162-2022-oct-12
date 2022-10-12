from enum import Enum


class AccountStatus(Enum):
    ACTIVE = 100
    CLOSED = 200
    BLOCKED = 300


class InsufficientBalanceError(Exception):
    def __init__(self, message, deficit):
        self.message = message
        self.deficit = deficit


# domain class -> entity: identity, solution class
class Account:
    # constructor
    def __init__(self, iban, balance=50, status=AccountStatus.ACTIVE):
        print("Account's Constructor is running...")
        self._iban = iban  # attribute/state/data/field
        self._balance = balance
        self._status = status

    # getter/setter

    @property
    def iban(self):  # read-only property
        print("getter Account::iban")
        return self._iban

    @property
    def balance(self):  # read-only property
        print("getter Account::balance")
        return self._balance

    @property
    def status(self):
        print("getter Account::status")
        return self._status

    @status.setter
    def status(self, status):
        if self._status == AccountStatus.CLOSED:
            raise ValueError("Cannot change status for a CLOSED account.")
        self._status = status

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("You must provide a positive amount.")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("You must provide a positive amount.")
        if amount > self._balance:
            deficit = amount - self._balance
            raise InsufficientBalanceError("Your balance does not cover your expenses.", deficit)
        self._balance -= amount
        return self._balance

    def __str__(self):
        return f"Account [iban: {self.iban}, balance: {self.balance}, status: {self.status.name} ({self.status.value})]"


"""
    Account         : Base   /Super/Parent Class
    CheckingAccount : Derived/Sub  /Child  Class
"""


class CheckingAccount(Account):
    def __init__(self, iban, balance=50, status=AccountStatus.ACTIVE, overdraftAmount=500):
        super().__init__(iban, balance, status)
        self._overdraftAmount = overdraftAmount

    @property
    def overdraftAmount(self):
        return self._overdraftAmount

    def withdraw(self, amount):  # overrides Account's withdraw
        if amount <= 0:
            raise ValueError("You must provide a positive amount.")
        if amount > (self.balance + self.overdraftAmount):
            deficit = amount - self.balance - self.overdraftAmount
            raise InsufficientBalanceError("Your balance does not cover your expenses.", deficit)
        self._balance -= amount
        return self.balance

    def __str__(self):  # overriding
        return f"CheckingAccount [iban: {self.iban}, balance: {self.balance}, status: {self.status.name} ({self.status.value}), " \
               f"overdraftAmount: {self.overdraftAmount}]"
