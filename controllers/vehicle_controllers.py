from fastapi import APIRouter, Path, Body
from config.db_helpers import get_vehicles_collection, get_repairs_collection
from models.vehicle_model import Trailer, Truck, Repair
from typing import Union
from helpers.vehicle_helper import post_vehicle_helper, set_trailer_to_truck, get_vehicle_helper, get_vehicles_helper, post_repair_helper, get_vehicle_repairs, update_vehicle_helper, delete_vehicle_helper

vehicle_router = APIRouter()

vehicles_collection = get_vehicles_collection()
repairs_collection = get_repairs_collection()

@vehicle_router.get('/vehicles', tags=["Vehicle routes"])
def get_vehicles():
    vehicles = get_vehicles_helper()
    return vehicles


@vehicle_router.get('/vehicles/{vehicle_id}', tags=["Vehicle routes"])
def get_vehicle(vehicle_id: str = Path(..., description="ID of the vehicle we want to get")):
    vehicle = get_vehicle_helper(vehicle_id)
    return vehicle


@vehicle_router.post('/vehicles', tags=["Vehicle routes"])
def post_vehicle(vehicle: Union[Truck, Trailer] = Body(..., description="Body of the vehicle we want to post")):
    vehicle = post_vehicle_helper(vehicle)
    return vehicle


@vehicle_router.put('/vehicles/{truck_id}/trailer/{trailer_id}', tags=["Vehicle routes"])
def set_trailer(truck_id: str = Path(..., description="ID of the truck we want to put the trailer to"), trailer_id: str = Path(..., description="ID of the trailer we want to put to the truck")):
    truck = set_trailer_to_truck(truck_id, trailer_id)
    return truck


@vehicle_router.post('/vehicles/{vehicle_id}/repair', tags=["Vehicle routes"])
def set_repair(vehicle_id: str = Path(..., description="ID of the vehicle that is getting repaired"), repair: Repair = Body(..., description="Body of the vehicles repair")):
    repair = post_repair_helper(vehicle_id, repair)
    return repair


@vehicle_router.get('/vehicles/{vehicle_id}/repair', tags=["Vehicle routes"])
def get_repairs(vehicle_id: str = Path(..., descripiton="ID of the vehicle we are requesting repairs from")):
    repairs = get_vehicle_repairs(vehicle_id)
    return repairs


@vehicle_router.patch('/vehicles/{vehicle_id}', tags=["Vehicle routes"])
def update_vehicle(vehicle_id: str = Path(..., description="ID of the vehicle we are updating"), vehicle: Union[Truck, Trailer] = Body(..., description="Body of the vehicle we are updating")):
    updated_vehicle = update_vehicle_helper(vehicle_id, vehicle)
    return updated_vehicle


@vehicle_router.delete('/vehicle/{vehicle_id}', tags=["Vehicle routes"])
def delete_vehicle(vehicle_id: str = Path(..., description="ID of the vehicle we are deleting")):
    delete_vehicle_helper(vehicle_id)