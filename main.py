from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory "database"
items = {}

# Data model
class Item(BaseModel):
    name: str
    price: float

# GET (root)
@app.get("/")
def read_root():
    return {"hello": "world"}

# GET all items
@app.get("/items")
def get_items():
    return items

# GET single item
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return items.get(item_id, {"error": "Item not found"})

# POST (create item)
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    items[item_id] = item
    return {"message": "Item created", "item": item}

# PUT (update item)
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        return {"error": "Item not found"}
    items[item_id] = item
    return {"message": "Item updated", "item": item}

# DELETE (remove item)
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        return {"error": "Item not found"}
    del items[item_id]
    return {"message": "Item deleted"}
