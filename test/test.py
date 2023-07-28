from fastapi import APIRouter
from fastapi.testclient import TestClient
from bson import ObjectId

from unittest import TestCase
import sys

sys.path.append('c:/Users/petar/OneDrive/Desktop/python/fastapi6')
from config.db_helpers import get_workers_collection
from controllers.worker_controllers import worker_router
test_client = TestClient(worker_router)
collection = get_workers_collection()

def test_route():
    test_body = {
      "first_name": "Nemar",
      "last_name": "Miric",
      "birthday": "29-03-1994",
      "jmbg": "smth",
      "age": 29,
      "exp": "none at all",
      "work_hours": 40,
      "area": "London",
      "role": "manager",
      "pay_per_month": 20000,
      "dispatchers_id": [],
      "truck_drivers_id": []
    }
    response = test_client.post('/workers', json=test_body)

    actual_worker = collection.find_one({"_id": ObjectId(response.json()["id"])}, {"_id": 0})

    TestCase().assertDictEqual(actual_worker, test_body)
