with open("accounts.txt", mode="rt") as accounts:
    for account in accounts:
        iban, balance, status = account.split(",")
        print(f"{iban}\t{balance}\t{status}")
