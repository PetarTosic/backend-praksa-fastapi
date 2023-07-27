from config.db_helpers import get_workers_collection
from helpers.vehicle_helper import set_truck_driver
from bson import ObjectId
from schemas.worker_schema import worker_serializer

collection = get_workers_collection()

def add_workers_ids_and_area(worker):
    if worker["role"] == 'truck driver':
        collection.update_one({"_id": ObjectId(worker["manager_id"])}, {"$push": {"truck_drivers_id": worker["id"]}})
        collection.update_one({"_id": ObjectId(worker["dispatcher_id"])}, {"$push": {"truck_drivers_id": worker["id"]}})
        manager = worker_serializer(collection.find_one({"_id": ObjectId(worker["manager_id"])}))
        collection.update_one({"_id": ObjectId(worker["id"])}, {"$set": {"area": manager["area"]}})
    
    if worker["role"] == 'dispatcher':
        collection.update_one({"_id": ObjectId(worker["manager_id"])}, {"$push": {"dispatchers_id": worker["id"]}})
        manager = worker_serializer(collection.find_one({"_id": ObjectId(worker["manager_id"])}))
        collection.update_one({"_id": ObjectId(worker["id"])}, {"$set": {"area": manager["area"]}})

def set_truck_to_driver(driver_id, truck_id):
    collection.update_one({"_id": ObjectId(driver_id)}, {"$set": {"truck_id": truck_id}})
    set_truck_driver(driver_id, truck_id)

def delete_dependencies(worker_id: str):
    worker = collection.find_one({"_id": ObjectId(worker_id)})

    if worker["role"] == 'truck driver':
        if worker["manager_id"] != "":
            collection.update_one({"_id": ObjectId(worker["dispatcher_id"])}, {"$pull": {"truck_drivers_id": worker_id}})
        if worker["dispatcher_id"] != "":
            collection.update_one({"_id": ObjectId(worker["manager_id"])}, {"$pull": {"truck_drivers_id": worker_id}})
        return
    
    if worker["role"] == 'dispatcher':
        if worker["manager_id"] != "":
            print(worker["manager_id"])
            collection.update_one({"_id": ObjectId(worker["manager_id"])}, {"$pull": {"dispatchers_id": worker_id}})
        for work_id in worker["truck_drivers_id"]:
            collection.update_one({"_id": ObjectId(work_id)}, {"$set": {"dispatcher_id": ""}})
        return
    
    for work_id in worker["truck_drivers_id"]:
        collection.update_one({"_id": ObjectId(work_id)}, {"$set": {"manager_id": ""}})
    for work_id in worker["dispatchers_id"]:
        collection.update_one({"_id": ObjectId(work_id)}, {"$set": {"manager_id": ""}})
    


    

