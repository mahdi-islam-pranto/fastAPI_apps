from fastapi import FastAPI
from pydantic import BaseModel


# initialize FastAPI
app = FastAPI()

# create class for Order parameters
class Order(BaseModel):
    units: int
    product: str

@app.get("/start")
async def start():
    return {"message": "Starting the FastAPI server"}

@app.get("/hello")
def hello(name: str = "Pranto"):
    return {"message": f"Hello {name}"}

@app.post("/order")
def order(orderParams: Order):
    return {"message": f"Order for {orderParams.units} units of {orderParams.product} is placed"}

