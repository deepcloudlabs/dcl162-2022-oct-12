import json

from kafka import KafkaConsumer
from pymongo import MongoClient

consumer = KafkaConsumer(
    "trades",
    bootstrap_servers=["localhost:9092"],
    group_id="algotrading",
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

mongo_client = MongoClient("mongodb://localhost:27017")
algotrading_db = mongo_client["algotrading"]
trades_collection = algotrading_db.trades

for message in consumer:
    trade = json.loads(message.value)
    print(trade)
    trades_collection.insert_one(trade)
