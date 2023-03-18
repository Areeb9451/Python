from operator import inv
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
# END POINT : An API endpoint is the point of entry in a communication channel when two system are intracting. It refers to touch points of the communication between API and a server.

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None , description = "The ID of the item you like to view", gt = 0)):
    return inventory[item_id]


@app.get("/get-by-name/{item_id}")
def get_item(test: int, item_id: int,name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not Found"}


@app.post("/create-item/{item_id}")
def create_item( item: Item, item_id = int):
    if item_id in inventory:
        return {"Error": "Item_ID Already Present"}
    inventory[item_id] = item
    return inventory[item_id]
