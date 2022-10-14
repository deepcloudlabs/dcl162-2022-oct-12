from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017")

banking_db = mongo_client["banking"]

accounts = [
    {"_id": "tr1", "balance": 100000, "status": "ACTIVE"},
    {"_id": "tr2", "balance": 200000, "status": "CLOSED"},
    {"_id": "tr3", "balance": 300000, "status": "ACTIVE"},
    {"_id": "tr4", "balance": 400000, "status": "BLOCKED"},
    {"_id": "tr5", "balance": 500000, "status": "ACTIVE"},
]

accounts_collection = banking_db.accounts

accounts_collection.insert_many(accounts)
accounts_collection.insert_one({"_id": "tr6", "balance": 600000, "status": "BLOCKED"})
