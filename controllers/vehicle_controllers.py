from fastapi import APIRouter
from config.db_helpers import get_vehicles_collection, get_repairs_collection
from schemas.vehicle_schema import vehicle_serializer, vehicles_serializer, repair_serializer, repairs_serializer
from bson import ObjectId
from models.vehicle_model import Trailer, Truck, Repair
from typing import Union
import json 
from helpers.vehicle_helper import set_trailer_to_truck, set_repair_to_vehicle

vehicle_router = APIRouter()

collection = get_vehicles_collection()
collection_repairs = get_repairs_collection()

@vehicle_router.get('/vehicles', tags=["Vehicle routes"])
def get_vehicles():
    vehicles = vehicles_serializer(collection.find())
    return vehicles


@vehicle_router.get('/vehicles/{vehicle_id}', tags=["Vehicle routes"])
def get_vehicle(vehicle_id: str):
    vehicle = vehicle_serializer(collection.find_one({"_id": ObjectId(vehicle_id)}))
    return vehicle


@vehicle_router.post('/vehicles', tags=["Vehicle routes"])
def post_vehicle(vehicle: Union[Truck, Trailer]):
    collection.insert_one(dict(vehicle))


@vehicle_router.put('/vehicles/{truck_id}/trailer', tags=["Vehicle routes"])
def set_trailer(truck_id: str, trailer_id: str):
    set_trailer_to_truck(truck_id, trailer_id)


@vehicle_router.post('/vehicles/{vehicle_id}/repair', tags=["Vehicle routes"])
def set_repair(vehicle_id: str, repair: Repair):
    response = collection_repairs.insert_one(dict(repair))
    repair = repair_serializer(collection_repairs.find_one({"_id": response.inserted_id}))
    set_repair_to_vehicle(vehicle_id, response.inserted_id)
    return repair


@vehicle_router.get('/vehicles/{vehicle_id}/repair', tags=["Vehicle routes"])
def get_repairs(vehicle_id: str):
    repairs = repairs_serializer(collection_repairs.find({"vehicle_id": vehicle_id}))
    return repairs


@vehicle_router.patch('/vehicles/{vehicle_id}', tags=["Vehicle routes"])
def update_vehicle(vehicle_id: str, vehicle: Union[Truck, Trailer]):
    collection.find_one_and_update({"_id": ObjectId(vehicle_id)}, {"$set": dict(vehicle)})


@vehicle_router.delete('/vehicle/{vehicle_id}', tags=["Vehicle routes"])
def delete_vehicle(vehicle_id: str):
    collection.delete_one({"_id": ObjectId(vehicle_id)})