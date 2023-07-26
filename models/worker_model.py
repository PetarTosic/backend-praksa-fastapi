from pydantic import BaseModel
from typing import Union

class Worker(BaseModel): 
    first_name: str
    last_name: str
    birthday: str
    jmbg: str
    age: int
    exp: str
    work_hours: int
    area: str
    role: str


class TruckDriver(Worker):
    pay_per_mile: int
    manager_id: str
    dispatcher_id: str
    truck_id: str | None


class Dispatcher(Worker):
    pay_per_month: int
    manager_id: str
    truck_drivers_id: Union[list[str], None]


class Manager(Worker):
    pay_per_month: int
    truck_drivers_id: Union[list[str], None]
    dispatchers_id: Union[list[str], None]