from fastapi import APIRouter
from config.db_helpers import get_vehicles_collection, get_repairs_collection
from schemas.vehicle_schema import vehicle_serializer, vehicles_serializer
from bson import ObjectId
from models.vehicle_model import Trailer, Truck
from typing import Union
import json 
from helpers.vehicle_helper import set_trailer_to_truck

vehicle_router = APIRouter()

collection = get_vehicles_collection()
collection_repairs = get_repairs_collection()

@vehicle_router.get('/vehicles')
def get_vehicles():
    vehicles = vehicles_serializer(collection.find())
    return vehicles


@vehicle_router.get('/vehicles/{vehicle_id}')
def get_vehicle(vehicle_id: str):
    vehicle = vehicle_serializer(collection.find_one({"_id": ObjectId(vehicle_id)}))
    return vehicle


@vehicle_router.post('/vehicles')
def post_vehicle(vehicle: Union[Truck, Trailer]):
    collection.insert_one(dict(vehicle))


@vehicle_router.put('/vehicles/{truck_id}/trailer')
def set_trailer(truck_id: str, trailer_id: str):
    set_trailer_to_truck(truck_id, trailer_id)