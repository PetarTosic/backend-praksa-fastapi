from config.db_helpers import get_workers_collection
from helpers.vehicle_helper import set_truck_driver
from bson import ObjectId

collection = get_workers_collection()

def add_workers_ids(worker):
    if worker["role"] == 'truck driver':
        collection.update_one({"_id": ObjectId(worker["manager_id"])}, {"$push": {"truck_drivers_id": worker["id"]}})
        collection.update_one({"_id": ObjectId(worker["dispatcher_id"])}, {"$push": {"truck_drivers_id": worker["id"]}})
    
    if worker["role"] == 'dispatcher':
        collection.update_one({"_id": ObjectId(worker["manager_id"])}, {"$push": {"dispatchers_id": worker["id"]}})

def set_truck_to_driver(driver_id, truck_id):
    collection.update_one({"_id": ObjectId(driver_id)}, {"$set": {"truck_id": truck_id}})
    set_truck_driver(driver_id, truck_id)
