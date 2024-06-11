from fastapi import FastAPI
from routers import TaskRouter

app = FastAPI(
    title="Extravaganza",
    description="developed as a newbie to the python's FastAPI",
)

@app.get("/")
def getStatus():
    return {"message":"server online"}

app.include_router(TaskRouter.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8095)