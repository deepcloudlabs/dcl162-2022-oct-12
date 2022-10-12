from random import random

from banking.domain import Account, CheckingAccount, AccountStatus

account = None

if random() < 0.5:
    print("Head")
    account = Account("TR1", 10000)
else:
    print("Tail")
    account = CheckingAccount("TR2", 20000, AccountStatus.ACTIVE, 1000)
account.withdraw(500)
print(account)
