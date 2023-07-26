from pydantic import BaseModel, Field
from typing import Union

class Repair(BaseModel):
    date: str
    description: str
    vehicle_id: Union[str, None]

class Vehicle(BaseModel):
    wheels: int
    miles: int
    year: int
    repairs_id: Union[list[str], None]
    role: str

class Trailer(Vehicle):
    type: str
    truck_id: Union[str, None]

class Truck(Vehicle):
    truck_driver_id: Union[str, None]
    trailer_id: Union[str, None]
    horsepower: int