from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017")

print("Database List\n=============")
for db_name in mongo_client.list_database_names():
    print(db_name)

world_db = mongo_client["world"]
print("\nCollection List in world\n========================")
for collection_name in world_db.list_collection_names():
    print(collection_name)
