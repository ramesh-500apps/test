from fastapi import FastAPI
from app import routers
from app.models import create_db_tables

app=FastAPI()
app.include_router(routers.router)

@app.on_event("startup")
def on_startup():
    create_db_tables()