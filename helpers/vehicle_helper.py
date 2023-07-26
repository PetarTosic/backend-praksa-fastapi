from config.db_helpers import get_vehicles_collection, get_repairs_collection
from bson import ObjectId

collection = get_vehicles_collection()

def set_trailer_to_truck(truck_id, trailer_id):
    collection.update_one({"_id": ObjectId(truck_id)}, {"$set": {"trailer_id": trailer_id}})
    collection.update_one({"_id": ObjectId(trailer_id)}, {"$set": {"truck_id": truck_id}})


def set_truck_driver(driver_id, truck_id):
    collection.update_one({"_id": ObjectId(truck_id)}, {"$set": {"truck_driver_id": driver_id}})