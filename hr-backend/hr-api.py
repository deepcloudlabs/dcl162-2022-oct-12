"""
mongodb
pymongo configuration
"""
import json

from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017")
hr_db = mongo_client["hrdb"]
employees = hr_db.employees

api = Flask(__name__)
api.config["DEBUG"] = True
cors = CORS(api)
socketio = SocketIO(api, cors_allowed_origins="*")


@api.route("/hr/api/v1/employees/<identity>", methods=["GET"])
def get_employee_by_identity(identity):
    return jsonify(employees.find_one({"_id": identity}))


@api.route("/hr/api/v1/employees", methods=["GET"])
def get_employees():
    return json.dumps([emp for emp in employees.find({})])
