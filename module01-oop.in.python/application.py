from banking.domain import Account, AccountStatus, InsufficientBalanceError, CheckingAccount

try:
    print(((0.1 + 0.2) + 0.3) == (0.1 + (0.2 + 0.3)))
    acc1 = Account("TR1", 1000, AccountStatus.ACTIVE)
    acc2 = CheckingAccount("TR2", 1000, AccountStatus.ACTIVE, 500)
    acc3 = Account("TR3")
    print(acc1.iban)
    print(acc1.balance)
    print(acc1.status)
    # acc1.status = AccountStatus.CLOSED  # triggers the setter method
    # acc1.status = AccountStatus.BLOCKED  # triggers the setter method
    acc2.withdraw(1500)  # withdraw(acc1, 1500) # self <- acc2
    # acc2.withdraw(0.1)
    print(acc2)
except ValueError as ve:
    print(ve)
except InsufficientBalanceError as ibe:
    print(f"{ibe.message}: {ibe.deficit}")
