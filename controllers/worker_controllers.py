from fastapi import APIRouter, Path, Body
from models.worker_model import TruckDriver, Manager, Dispatcher
from config.db_helpers import get_workers_collection
from typing import Union
from helpers.worker_helper import delete_worker_helper, update_worker_helper, post_worker_helper, get_worker_helper, get_workers_helper, set_truck_to_driver

worker_router = APIRouter()

workers_collection = get_workers_collection()

@worker_router.get('/workers', tags=["Worker routes"])
def get_workers():
    workers = get_workers_helper()
    return workers


@worker_router.get('/workers/{worker_id}', tags=["Worker routes"])
def get_worker(worker_id: str = Path(..., description="ID of the worker we want to get")):
    worker = get_worker_helper(worker_id)
    return worker


@worker_router.post('/workers', tags=["Worker routes"])
def post_worker(worker: Union[TruckDriver, Manager, Dispatcher] = Body(..., description="Body of the worker we want to post")):
    worker = post_worker_helper(worker)
    return worker


@worker_router.put('/workers/{worker_id}/truck/{truck_id}', tags=["Worker routes"])
def set_truck(worker_id: str = Path(..., description="ID of the truck driver"), truck_id: str = Path(..., description="ID of the truck")):
    worker = set_truck_to_driver(worker_id, truck_id)
    return worker


@worker_router.patch('/workers/{worker_id}', tags=["Worker routes"])
def update_worker(worker_id: str = Path(..., description="ID of the worker we want to update"), worker: Union[TruckDriver, Manager, Dispatcher] = Body(..., description="Body of the worker we want to update")):
    worker = update_worker_helper(worker_id, worker)
    return worker


@worker_router.delete('/workers/{worker_id}', tags=["Worker routes"])
def delete_worker(worker_id: str = Path(..., description="ID of the worker we want to delete")):
    delete_worker_helper(worker_id)