from fastapi import FastAPI
from routers import init_routes

app = FastAPI()
init_routes()
