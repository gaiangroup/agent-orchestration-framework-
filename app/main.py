from fastapi import FastAPI
from app.routers.Variable_Route import variableRouter
app = FastAPI()

app.include_router(variableRouter)
