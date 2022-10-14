from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017")

banking_db = mongo_client["banking"]

accounts = [
    {"_id": "tr10", "balance": 100000, "status": "ACTIVE"},
    {"_id": "tr20", "balance": 200000, "status": "CLOSED"},
    {"_id": "tr30", "balance": 300000, "status": "ACTIVE"},
    {"_id": "tr40", "balance": 400000, "status": "BLOCKED"},
    {"_id": "tr50", "balance": 500000, "status": "ACTIVE"},
]

accounts_collection = banking_db.accounts

accounts_collection.insert_many(accounts)
accounts_collection.insert_one({"_id": "tr60", "balance": 600000, "status": "CLOSED"})
