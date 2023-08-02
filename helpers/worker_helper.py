from config.db_helpers import get_workers_collection
from helpers.vehicle_helper import set_truck_driver
from bson import ObjectId
from schemas.worker_schema import worker_serializer, workers_serializer

workers_collection = get_workers_collection()

def add_workers_ids_and_area(worker):
    if worker["role"] == 'truck driver':
        workers_collection.update_one({"_id": ObjectId(worker["manager_id"])}, {"$push": {"truck_drivers_id": worker["id"]}})
        workers_collection.update_one({"_id": ObjectId(worker["dispatcher_id"])}, {"$push": {"truck_drivers_id": worker["id"]}})
        manager = worker_serializer(workers_collection.find_one({"_id": ObjectId(worker["manager_id"])}))
        workers_collection.update_one({"_id": ObjectId(worker["id"])}, {"$set": {"area": manager["area"]}})
    
    if worker["role"] == 'dispatcher':
        workers_collection.update_one({"_id": ObjectId(worker["manager_id"])}, {"$push": {"dispatchers_id": worker["id"]}})
        manager = worker_serializer(workers_collection.find_one({"_id": ObjectId(worker["manager_id"])}))
        workers_collection.update_one({"_id": ObjectId(worker["id"])}, {"$set": {"area": manager["area"]}})

def set_truck_to_driver(driver_id, truck_id):
    workers_collection.update_one({"_id": ObjectId(driver_id)}, {"$set": {"truck_id": truck_id}})
    set_truck_driver(driver_id, truck_id)
    return get_worker_helper(driver_id)

def delete_dependencies(worker_id: str):
    worker = workers_collection.find_one({"_id": ObjectId(worker_id)})

    if worker["role"] == 'truck driver':
        if worker["manager_id"] != "":
            workers_collection.update_one({"_id": ObjectId(worker["dispatcher_id"])}, {"$pull": {"truck_drivers_id": worker_id}})
        if worker["dispatcher_id"] != "":
            workers_collection.update_one({"_id": ObjectId(worker["manager_id"])}, {"$pull": {"truck_drivers_id": worker_id}})
        return
    
    if worker["role"] == 'dispatcher':
        if worker["manager_id"] != "":
            print(worker["manager_id"])
            workers_collection.update_one({"_id": ObjectId(worker["manager_id"])}, {"$pull": {"dispatchers_id": worker_id}})
        for work_id in worker["truck_drivers_id"]:
            workers_collection.update_one({"_id": ObjectId(work_id)}, {"$set": {"dispatcher_id": ""}})
        return
    
    for work_id in worker["truck_drivers_id"]:
        workers_collection.update_one({"_id": ObjectId(work_id)}, {"$set": {"manager_id": ""}})
    for work_id in worker["dispatchers_id"]:
        workers_collection.update_one({"_id": ObjectId(work_id)}, {"$set": {"manager_id": ""}})
    

def get_workers_helper():
    return workers_serializer(workers_collection.find())

    
def get_worker_helper(worker_id):
    return worker_serializer(workers_collection.find_one({"_id": ObjectId(worker_id)}))


def post_worker_helper(worker):
    response = workers_collection.insert_one(dict(worker))
    add_workers_ids_and_area(worker)
    return worker_serializer(workers_collection.find_one({"_id": response.inserted_id}))


def update_worker_helper(worker_id, worker):
    workers_collection.find_one_and_update({"_id": ObjectId(worker_id)}, {"$set": dict(worker)})
    return get_worker_helper(worker_id)


def delete_worker_helper(worker_id):
    delete_dependencies(worker_id)
    workers_collection.delete_one({"_id": ObjectId(worker_id)})