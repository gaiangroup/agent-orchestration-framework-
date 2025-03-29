from fastapi import FastAPI
from app.routers.Variable_Route import variableRouter
app = FastAPI()

app.include_router(variableRouter)

@app.get("/")
async def root():
    return {"message": "Hello World"}