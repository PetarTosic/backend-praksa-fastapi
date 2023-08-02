from config.db_helpers import get_vehicles_collection, get_repairs_collection
from bson import ObjectId
from schemas.vehicle_schema import vehicle_serializer, vehicles_serializer, repair_serializer, repairs_serializer

vehicles_collection = get_vehicles_collection()
repairs_collection = get_repairs_collection()

def set_trailer_to_truck(truck_id, trailer_id):
    vehicles_collection.update_one({"_id": ObjectId(truck_id)}, {"$set": {"trailer_id": str(trailer_id)}})
    vehicles_collection.update_one({"_id": ObjectId(trailer_id)}, {"$set": {"truck_id": str(truck_id)}})
    return get_vehicle_helper(truck_id)


def set_truck_driver(driver_id, truck_id):
    vehicles_collection.update_one({"_id": ObjectId(truck_id)}, {"$set": {"truck_driver_id": str(driver_id)}})


def set_repair_to_vehicle(vehicle_id, repair_id):
    vehicles_collection.update_one({"_id": ObjectId(vehicle_id)}, {"$push": {"repairs_id": str(repair_id)}})


def get_vehicle_helper(vehicle_id):
    return vehicle_serializer(vehicles_collection.find_one({"_id": ObjectId(vehicle_id)}))


def get_vehicles_helper():
    return vehicles_serializer(vehicles_collection.find())
    

def post_vehicle_helper(vehicle):
    response = vehicles_collection.insert_one(dict(vehicle))
    vehicle = get_vehicle_helper(response.inserted_id)
    return vehicle

def post_repair_helper(vehicle_id, repair):
    response = repairs_collection.insert_one(dict(repair))
    set_repair_to_vehicle(vehicle_id, response.inserted_id)
    repair = repair_serializer(repairs_collection.find_one({"_id": response.inserted_id}))
    return repair


def get_vehicle_repairs(vehicle_id):
    return repairs_serializer(repairs_collection.find({"vehicle_id": vehicle_id}))


def update_vehicle_helper(vehicle_id, vehicle):
    vehicles_collection.find_one_and_update({"_id": ObjectId(vehicle_id)}, {"$set": dict(vehicle)})
    return get_vehicle_helper(vehicle_id)


def delete_vehicle_helper(vehicle_id):
    vehicles_collection.delete_one({"_id": ObjectId(vehicle_id)})
