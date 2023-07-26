
def vehicle_serializer(vehicle) -> dict:
    if vehicle["role"] == "truck":
      return {
          "id": str(vehicle["_id"]),
          "wheels": vehicle["wheels"],
          "miles": vehicle["miles"],
          "year": vehicle["year"],
          "repairs_id": vehicle["repairs_id"],
          "truck_driver_id": vehicle["truck_driver_id"],
          "trailer_id": vehicle["trailer_id"],
          "horsepower": vehicle["horsepower"],
          "role": vehicle["role"]
      }
    else:
        return {
        "id": str(vehicle["_id"]),
        "wheels": vehicle["wheels"],
        "miles": vehicle["miles"],
        "year": vehicle["year"],
        "repairs_id": vehicle["repairs_id"],
        "type": vehicle["type"],
        "truck_id": vehicle["truck_id"],
        "role": vehicle["role"]
    }

def vehicles_serializer(vehicles) -> list:
    return [vehicle_serializer(vehicle) for vehicle in vehicles]


def repair_serializer(repair) -> dict:
    return {
        "id": str(repair["_id"]),
        "date": repair["date"],
        "description": repair["description"],
        "vehicle_id": repair["vehicle_id"]
    }

def repairs_serializer(repairs) -> list:
    return [repair_serializer(repair) for repair in repairs]