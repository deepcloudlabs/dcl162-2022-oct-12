from banking.domain import Account, AccountStatus

acc1 = Account("TR1", 1000, AccountStatus.ACTIVE)
acc2 = Account("TR2", 1000)
acc3 = Account("TR3")
print(acc1.iban)
print(acc1.balance)
print(acc1.status)
# acc1.status = AccountStatus.CLOSED  # triggers the setter method
# acc1.status = AccountStatus.BLOCKED  # triggers the setter method
# acc1.withdraw(1000000)
print(acc1.iban)