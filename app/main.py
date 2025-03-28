from fastapi import FastAPI
from routers import Instructions_Route

app = FastAPI(title="Agent Orchestration Framework")

# Include API routes
app.include_router(Instructions_Route.instruction_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
