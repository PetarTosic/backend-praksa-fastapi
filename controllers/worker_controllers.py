from fastapi import APIRouter, HTTPException, Response, status
from models.worker_model import TruckDriver, Manager, Dispatcher
from config.db_helpers import get_workers_collection
from schemas.worker_schema import worker_serializer, workers_serializer
from bson import ObjectId, json_util
from typing import Union
from helpers.worker_helper import add_workers_ids, set_truck_to_driver

worker_router = APIRouter()

collection = get_workers_collection()

@worker_router.get('/workers')
def get_workers():
    workers = workers_serializer(collection.find())
    return workers


@worker_router.get('/workers/{worker_id}')
def get_worker(worker_id: str):
    worker = worker_serializer(collection.find_one({"_id": ObjectId(worker_id)}))
    return worker


@worker_router.post('/workers')
def post_worker(worker: Union[TruckDriver, Manager, Dispatcher]):
    response = collection.insert_one(dict(worker))
    worker = worker_serializer(collection.find_one({"_id": response.inserted_id}))
    add_workers_ids(worker)
    return worker


@worker_router.put('/workers/{worker_id}/truck')
def set_truck(worker_id: str, truck_id: str):
    set_truck_to_driver(worker_id, truck_id)