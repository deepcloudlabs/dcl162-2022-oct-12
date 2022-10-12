from banking.domain import Account, CheckingAccount, AccountStatus

bank_accounts = [
    Account("TR1", 10000),
    CheckingAccount("TR2", 20000, AccountStatus.CLOSED, 1000),
    Account("TR3", 30000),
    CheckingAccount("TR4", 40000, AccountStatus.BLOCKED, 4000),
    Account("TR5", 50000),
    CheckingAccount("TR6", 60000, AccountStatus.CLOSED, 6000),
]


def withdrawMoney(accounts, amount):
    for account in accounts:
        if account.status == AccountStatus.ACTIVE:
            if isinstance(account, Account):
                account.withdraw(2*amount)
            else:
                account.withdraw(amount)


withdrawMoney(bank_accounts, 50)
for account in bank_accounts:
    print(account)
