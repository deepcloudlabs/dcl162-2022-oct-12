import pickle

with open("accounts.pkl", mode="rb") as f:
    accounts = pickle.load(f)
    for account in accounts:
        print(account)
