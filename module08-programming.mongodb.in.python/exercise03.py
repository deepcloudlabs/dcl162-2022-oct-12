from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017")

banking_db = mongo_client["banking"]

accounts_collection = banking_db.accounts

print("ALL ACTIVE ACCOUNTS:")
for account in accounts_collection.find({"status": "ACTIVE"}, {"balance": False}):
    print(account)

# http://binkurt.blogspot.com/2015/02/mongodb-ile-calsmak.html
print("\nACCOUNTS (balance > 200k & status=CLOSED):")
for account in accounts_collection.find({"$and": [{"balance": {"$gt": 200000}}, {"status": "BLOCKED"}]},
                                        {"balance": True}):
    print(account)
