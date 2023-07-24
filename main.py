from fastapi import FastAPI
from controllers.user_controllers import user_router

app = FastAPI()

app.include_router(user_router)