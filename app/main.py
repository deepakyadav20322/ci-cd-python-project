from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def testing_route():
    return {"Hello": "World"}


@app.get("/health")
async def health_check():
    return {"message": "Api health check successful"}
