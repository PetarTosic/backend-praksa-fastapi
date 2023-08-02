from fastapi import FastAPI
from controllers.user_controllers import user_router
from controllers.worker_controllers import worker_router
from controllers.vehicle_controllers import vehicle_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials = True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["*"]
)

app.include_router(user_router)
app.include_router(worker_router)
app.include_router(vehicle_router)