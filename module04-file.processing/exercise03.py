import pickle

accounts = [
    ["TR1", 1000, "ACTIVE"],
    ["TR2", 2000, "CLOSED"],
    ["TR3", 3000, "ACTIVE"],
    ["TR4", 4000, "BLOCKED"],
    ["TR5", 5000, "ACTIVE"]
]

with open("accounts.pkl", mode="wb") as f:
    pickle.dump(accounts, f)
