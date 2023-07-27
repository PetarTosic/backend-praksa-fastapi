from config.db_helpers import get_vehicles_collection, get_repairs_collection
from bson import ObjectId

collection = get_vehicles_collection()

def set_trailer_to_truck(truck_id, trailer_id):
    collection.update_one({"_id": ObjectId(truck_id)}, {"$set": {"trailer_id": str(trailer_id)}})
    collection.update_one({"_id": ObjectId(trailer_id)}, {"$set": {"truck_id": str(truck_id)}})


def set_truck_driver(driver_id, truck_id):
    collection.update_one({"_id": ObjectId(truck_id)}, {"$set": {"truck_driver_id": str(driver_id)}})


def set_repair_to_vehicle(vehicle_id, repair_id):
    collection.update_one({"_id": ObjectId(vehicle_id)}, {"$push": {"repairs_id": str(repair_id)}})