from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Get the database and collection
db = client["mydatabase"]
col = db["mycollection"]

@app.post("/items/")
async def create_item(item: dict):
    # Insert the item into the collection
    result = col.insert_one(item)
    return {"id": str(result.inserted_id)}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    # Find the item by its ID
    item = col.find_one({"_id": item_id})
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: str, item: dict):
    # Update the item in the collection
    result = col.replace_one({"_id": item_id}, item)
    return {"updated": result.modified_count}

@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    # Delete the item from the collection
    result = col.delete_one({"_id": item_id})
    return {"deleted": result.deleted_count}
