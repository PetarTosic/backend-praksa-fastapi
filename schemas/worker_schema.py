
def worker_serializer(worker) -> dict:
    if worker["role"] == "truck driver":
        return {
            "id": str(worker["_id"]), 
            "first_name": worker["first_name"],
            "last_name": worker["last_name"],
            "birthday": worker["birthday"],
            "jmbg": worker["jmbg"],
            "age": worker["age"],
            "exp": worker["exp"],
            "work_hours": worker["work_hours"],
            "area": worker["area"],
            "pay_per_mile": worker["pay_per_mile"],
            "manager_id": worker["manager_id"],
            "dispatcher_id": worker["dispatcher_id"],
            "truck_id": worker["truck_id"],
            "role": worker["role"]
        }
    if worker["role"] == "dispatcher":
        return {
            "id": str(worker["_id"]), 
            "first_name": worker["first_name"],
            "last_name": worker["last_name"],
            "birthday": worker["birthday"],
            "jmbg": worker["jmbg"],
            "age": worker["age"],
            "exp": worker["exp"],
            "work_hours": worker["work_hours"],
            "area": worker["area"],
            "pay_per_month": worker["pay_per_month"],
            "manager_id": worker["manager_id"],
            "truck_drivers_id": worker["truck_drivers_id"],
            "role": worker["role"]
        }
    return {
        "id": str(worker["_id"]), 
        "first_name": worker["first_name"],
        "last_name": worker["last_name"],
        "birthday": worker["birthday"],
        "jmbg": worker["jmbg"],
        "age": worker["age"],
        "exp": worker["exp"],
        "work_hours": worker["work_hours"],
        "area": worker["area"],
        "pay_per_month": worker["pay_per_month"],
        "truck_drivers_id": worker["truck_drivers_id"],
        "dispatchers_id": worker["dispatchers_id"],
        "role": worker["role"]
    }

def workers_serializer(workers) -> list:
    return [worker_serializer(worker) for worker in workers]