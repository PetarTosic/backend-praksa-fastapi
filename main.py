from fastapi import FastAPI
from controllers.user_controllers import user_router
from controllers.worker_controllers import worker_router
from controllers.vehicle_controllers import vehicle_router

app = FastAPI()

app.include_router(user_router)
app.include_router(worker_router)
app.include_router(vehicle_router)