from fastapi import APIRouter, HTTPException, Response, status
from models.worker_model import TruckDriver, Manager, Dispatcher
from config.db_helpers import get_workers_collection
from schemas.worker_schema import worker_serializer, workers_serializer
from bson import ObjectId, json_util
from typing import Union
from helpers.worker_helper import add_workers_ids_and_area, set_truck_to_driver, delete_dependencies

worker_router = APIRouter()

collection = get_workers_collection()

@worker_router.get('/workers', tags=["Worker routes"])
def get_workers():
    workers = workers_serializer(collection.find())
    return workers


@worker_router.get('/workers/{worker_id}', tags=["Worker routes"])
def get_worker(worker_id: str):
    worker = worker_serializer(collection.find_one({"_id": ObjectId(worker_id)}))
    return worker


@worker_router.post('/workers', tags=["Worker routes"])
def post_worker(worker: Union[TruckDriver, Manager, Dispatcher]):
    response = collection.insert_one(dict(worker))
    worker = worker_serializer(collection.find_one({"_id": response.inserted_id}))
    add_workers_ids_and_area(worker)
    return worker


@worker_router.put('/workers/{worker_id}/truck', tags=["Worker routes"])
def set_truck(worker_id: str, truck_id: str):
    set_truck_to_driver(worker_id, truck_id)


@worker_router.patch('/workers/{worker_id}', tags=["Worker routes"])
def update_worker(worker_id: str, worker: Union[TruckDriver, Manager, Dispatcher]):
    collection.find_one_and_update({"_id": ObjectId(worker_id)}, {"$set": dict(worker)})


@worker_router.delete('/workers/{worker_id}', tags=["Worker routes"])
def delete_worker(worker_id: str):
    delete_dependencies(worker_id)
    collection.delete_one({"_id": ObjectId(worker_id)})
