from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def testing_route():
    return {"Hello": "World"}

